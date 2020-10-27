# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 11:21:12 2019

@author: LukaszMalucha
"""


import pandas as pd


dataset = pd.read_csv('companies.csv', error_bad_lines=False)
dataset = dataset.dropna()

# drop old header rows
dataset = dataset[dataset.name != 'name']

# clean name
dataset['name'] = dataset['name'].str.title()

# clean company type
dataset['companyType'] = dataset['companyType'].str.replace('Self Owned','Self Employed')


# clean employee count
dataset['employeeCountRange'] = dataset['employeeCountRange'].str.replace('myself only','1-50')


# specialities cleaner
dataset = dataset.rename(columns={'specialties': 'specialities'})
dataset['specialities'] = dataset['specialities'].str.replace(', ',',')
dataset['specialities'] = dataset['specialities'].str.replace(',',', ')
dataset['specialities'] = dataset['specialities'].str.split(', ')
dataset.loc[:, "specialities"] = dataset.specialities.map(lambda x: x[:3]) # leave only first three
dataset['specialities'] = dataset['specialities'].str.join(', ')
dataset['specialities'] = dataset['specialities'].str.lower()


# website url cleaner
dataset['websiteUrl'] = dataset['websiteUrl'].str.replace('http://','')
dataset['websiteUrl'] = dataset['websiteUrl'].str.replace('https://','')
dataset['websiteUrl'] = dataset['websiteUrl'].str.replace('/www.','')
dataset['websiteUrl'] = dataset['websiteUrl'].str.replace('www.','')
dataset['websiteUrl'] = 'http://www.' + dataset['websiteUrl']

dataset.loc[(dataset['name'] == "Depfa Bank"), 'websiteUrl'] = "http://www.depfa.com/"
dataset.loc[(dataset['name'] == "National College of Business Administration (NCBA)."), 'websiteUrl'] = "http://www.masterstudies.com/universities/Ireland/NCBA/"
dataset.loc[(dataset['name'] == "Harvest Financial Services"), 'websiteUrl'] = "http://www.harvestfinancial.ie/"

# group cleaner
dataset['group'] = dataset['group'].str.replace('EDUCATION','education')
dataset['group'] = dataset['group'].str.replace('Financial','finance')
dataset['group'] = dataset['group'].str.replace('IT','it')

dataset.to_csv("companies.csv", index = False, encoding = "utf-8")

