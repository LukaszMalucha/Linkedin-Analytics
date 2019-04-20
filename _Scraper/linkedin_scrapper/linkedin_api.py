import os
import json
import env_linkedin
from linkedin import linkedin
from oauthlib import *


## CREDENTIALS

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')               ## hidden
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')         ## hidden
OAUTH_TOKEN = os.environ.get('OAUTH_TOKEN')                 ## hidden
OAUTH_TOKEN_SECRET = os.environ.get('OAUTH_TOKEN_SECRET')   ## hidden


RETURN_URL = 'http://localhost:8000'

authentication = linkedin.LinkedInDeveloperAuthentication(CONSUMER_KEY, CONSUMER_SECRET, 
                                                      OAUTH_TOKEN, OAUTH_TOKEN_SECRET, 
                                                      RETURN_URL, linkedin.PERMISSIONS.enums.values())
                                                      
                                                      
application = linkedin.LinkedInApplication(authentication)        



def collect_pages(m, count):
    for i in range(count):
        pages.append(i + m)
    return pages


### COMPANIES DICTIONARY - THROTTLE LIMIT PER TOKEN PER DAY - 500 SEARCHES
### SELECTORS - https://developer.linkedin.com/docs/fields/company-profile
### IRELAND = 'facet' : ['location,ie:0']

# FINANCE
# companies = application.search_company(selectors=[{'companies': ['name']}], 
#                                                                  params={ 'facet' : ['location,ie:0','industry,47,41,129,43,42,44,45,46,128,106'] })
                                                                 
# EDUCATION
companies = application.search_company(selectors=[{'companies': ['name']}], 
                                                                 params={ 'facet' : ['location,ie:0','industry,69,132,68,105'] })                                                                 
                                                                 

## Scraper Iterator

total = companies['companies']['_total']
count = int(total / 20)
pages= [0,] 
collect_pages(20, count)

 
## SCRAPING
 
companies_EDU = []    
for element in pages:
    comps = application.search_company(selectors=[{'companies': ['name', 'website-url', 'specialties','company-type',
                                                                 'square-logo-url','industries','employee-count-range',
                                                                 'founded-year','num-followers',]}],  params={'facet' : ['location,ie:0','industry,69,132,68,105'], 'count': 20, 'start': element})
    companies_EDU.append(comps)
        
## SAVE AS JSON        
        
with open('companies_EDU.json', 'w') as outfile:
        json.dump(companies_EDU, outfile, indent=4)        
