import csv
import json
import os.path
import re

import pandas as pd
from django.conf import settings
from sklearn.preprocessing import MultiLabelBinarizer

from core.models import Company

# FILE PATHS


companies_path = os.path.join(settings.BASE_DIR, "db_manager/datasets/companies.csv")
finance_sector = os.path.join(settings.BASE_DIR, "db_manager/datasets/finance.json")
it_sector = os.path.join(settings.BASE_DIR, "db_manager/datasets/it.json")
education_sector = os.path.join(settings.BASE_DIR, "db_manager/datasets/education.json")


def database_upload():
    """Upload scraped data to db"""
    companies = Company.objects.all()
    companies.delete()

    if companies_path:
        with open(companies_path, encoding="utf8") as f:
            reader = csv.reader(f)  # skip header
            next(reader, None)
            for row in reader:
                try:
                    _, created = Company.objects.get_or_create(name=row[0], companyType=row[1],
                                                               employeeCountRange=row[2],
                                                               foundedYear=row[3], industries=row[4],
                                                               numFollowers=row[5], specialities=row[6],
                                                               squareLogoUrl=row[7], websiteUrl=row[8], group=row[9]
                                                               )
                except:
                    pass
    else:
        pass


def sector_insights(sector):
    """Sector companies details"""

    if sector == 'finance':
        sector_strings = ['Financial Companies', 'finance']

    elif sector == 'education':
        sector_strings = ['Educational Institutions', 'education']
    else:
        sector_strings = ['IT Companies', 'it']

    # Django queryset to pandas dataframe for analytics:

    dataset = pd.DataFrame(list(Company.objects.filter(group=sector).values()))

    # Number of companies

    count = len(dataset)

    # Companies with longest tradition

    oldest_10 = dataset.iloc[:, [4, 1]].sort_values(by=['foundedYear'])[:10]
    oldest_10_dict = oldest_10.to_dict(orient="records")

    # Get the most common specialities in the dataset

    clean_specialities = []
    for element in dataset['specialities']:
        element = element.replace("[", "")
        element = element.replace("]", "")
        element = element.replace("'", "")
        element = element.strip()
        clean_specialities.append(element)

    df_spec = pd.DataFrame()
    df_spec['clean_specialities'] = clean_specialities

    spec_list = []
    for element in df_spec['clean_specialities']:
        specs = element.split(',')
        spec_list.append(specs)

    specs_area = pd.DataFrame()
    specs_area['specialities_list'] = spec_list

    # Specs featurization

    mlb = MultiLabelBinarizer()

    new_array = mlb.fit_transform(specs_area['specialities_list'])
    spec_classes = list(mlb.classes_)
    df_specs_transformed = pd.DataFrame(data=new_array, columns=spec_classes)

    spec_total = df_specs_transformed.sum(axis=0).sort_values(ascending=False)[
                 1:28]  # omitt "not specified most common"
    spec_dict = spec_total.to_dict()

    # Most popular Company type

    type_values = dataset['companyType'].value_counts()[:6]
    type_dict = type_values.to_dict()

    # Companies by employee count

    e_count_values = dataset['employeeCountRange'].value_counts()
    e_count_dict = e_count_values.to_dict()

    # Companies by number of followers

    followers_values = dataset['numFollowers'].value_counts()
    followers_dict = followers_values.to_dict()

    sector_dict = {'count': count,
                   'oldest_10_dict': oldest_10_dict,
                   'sector_strings': sector_strings,
                   'spec_dict': spec_dict,
                   'type_dict': type_dict,
                   'e_count_dict': e_count_dict,
                   'followers_dict': followers_dict}

    with open(f'db_manager/datasets/{sector}.json', 'w') as file:
        json.dump(sector_dict, file)


def sector_listing(sector):
    """List of Sector Companies"""

    if sector == 'finance':
        sector = 'Financial'
        sector_strings = ['Financial Companies', 'finance']
    elif sector == 'education':
        sector = 'EDUCATION'
        sector_strings = ['Educational Institutions', 'education']
    else:
        sector = "IT"
        sector_strings = ['IT Companies', 'it']

    sector_companies = Company.objects.filter(group=sector).values()

    # Hacky! data cleaner to be fixed in future
    for element in sector_companies:
        for key, val in element.items():
            if key == 'specialities':
                element[key] = re.sub(',', ', ', val)
            if key == 'industries':
                element[key] = re.sub(' & Services', '', val)

    sector_companies = sorted(sector_companies, key=lambda k: k['name'])

    count = len(sector_companies)

    companies_dict = {'sector_companies': sector_companies, "count": count,
                      'sector_strings': sector_strings}

    return companies_dict
