# LinkedIn Analytics

#### [Visit the App](https://linkedinanalytics1.herokuapp.com/)

<br>

![1](https://user-images.githubusercontent.com/26208598/54323062-84431580-45ef-11e9-9598-17a44a6efc29.JPG)

<br>

## Project Description

Django interface for LinkedIn data extraction. Easily adjustable functionality, with REST API. 
Database hosts Irish companies (location: Ireland) from three sectors: financial, IT & education. 
Find out more with statistical data dashboard about a sector or search for more information regarding chosen company.


## App Views

### Main Dashboard
##### `/`
Choose one of three diffrent sector insights or find company information via searchbox

###### Scrapers:

Data was scraped with Scrapy + Selenium combo v& LinkedIn API.

###### Data Preprocessing:
Dataset was preprocessed with pandas. 
<br>
<br>

![1](https://user-images.githubusercontent.com/26208598/54323062-84431580-45ef-11e9-9598-17a44a6efc29.JPG)

#### Sector Insights:
##### `/companies/**`
Classical database analytics done with pandas, scikitlearn and Chart.js
<br>
<br>

![2](https://user-images.githubusercontent.com/26208598/54323063-84431580-45ef-11e9-8302-60f5bdef0e66.JPG)

#### Sector Listing:
##### `insights/list/**`
Full Company listing view
<br>
<br>

![3](https://user-images.githubusercontent.com/26208598/54323064-84dbac00-45ef-11e9-89a2-3fa39aa7bb48.JPG)

#### Search Results View:
##### `/insights/company_search`
Datasets comparison with pandas and chartJs
<br>
<br>

![4](https://user-images.githubusercontent.com/26208598/54323065-84dbac00-45ef-11e9-8515-a9e330b8af41.JPG)

 
### Manage User
#### `/user/my_account/`

![5](https://user-images.githubusercontent.com/26208598/54323066-84dbac00-45ef-11e9-91a6-c3c0f4da85e0.JPG)

<br>
<br>





-----------------

## Django REST Endpoints

#### Navigation
##### `/rest`

![6](https://user-images.githubusercontent.com/26208598/54323067-84dbac00-45ef-11e9-9baa-f4d0cb78c044.JPG)

<br>
<br>

#### User
##### `api/user`

 User handling via RESTFUL Api with Token Authorization.

![8](https://user-images.githubusercontent.com/26208598/54323069-85744280-45ef-11e9-9c9f-2f2ea1420e82.JPG)

<br>
<br>



#### Companies 
##### `/api/companies/`

Apply Property Value Estimator algorithm via RESTFul Api.
 
![9](https://user-images.githubusercontent.com/26208598/54323070-85744280-45ef-11e9-834e-a1afcfd51993.JPG) 

<br>


-----------------



## TOOLS, MODULES & TECHNIQUES

### Travis CI:

[![Build Status](https://travis-ci.com/LukaszMalucha/Linkedin-Analytics.svg?branch=master)](https://travis-ci.com/LukaszMalucha/Linkedin-Analytics)

### Test Files:
#### `/core/tests/`

##### Web Development:
Django | Django RESTful | Docker | Heroku | Bootstrap | Materialize | AWS S3

##### Database Development:
Postgres | SQLite

##### Python & JS – data analysis & visualisation:
pandas | numpy | scikit-learn | chart.js

##### Testing
Django.test

##### LinkedIn API with Python 
https://github.com/ozgur/python-linkedin

<br>
<br>

##### Thank you,

Lukasz Malucha
