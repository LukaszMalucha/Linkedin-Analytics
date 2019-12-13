# LinkedIn Analytics

#### [Visit the App](https://linkedinanalytics.herokuapp.com/)

<br>

![2](https://user-images.githubusercontent.com/26208598/70807515-9a1b7c00-1db5-11ea-9935-66a94c83b288.PNG)

<br>

## Project Description

Django interface for LinkedIn API data extraction. Easily adjustable functionality, with REST API backend and Vue.js frontend 
features like dynamic search. Database hosts Irish companies (location: Ireland) from three sectors: financial, IT & education. 
Find out more with statistical data dashboard about a sector or search for more information regarding chosen company.


## App Views

### Main Dashboard
##### `/`
Choose one of three different sector insights or find company information via searchbox

###### Scrapers:

Data was scraped with Scrapy + Selenium combo v& LinkedIn API.

###### Data Preprocessing:
Dataset was preprocessed with pandas. 
<br>
<br>

![1](https://user-images.githubusercontent.com/26208598/70807514-9a1b7c00-1db5-11ea-9b6d-7e8b1402e122.PNG)

#### Sector Insights:
##### `/[finance, it, education]`
Classical database analytics done with pandas, scikitlearn and Chart.js
<br>
<br>

![2](https://user-images.githubusercontent.com/26208598/70807515-9a1b7c00-1db5-11ea-9935-66a94c83b288.PNG)

#### Sector Listing:
##### `companies/[finance, it, education]`
Full Company listing view
<br>
<br>

![3](https://user-images.githubusercontent.com/26208598/70807516-9a1b7c00-1db5-11ea-9dba-ac649bb16ce3.PNG)

#### Dynamic Search:
<br>
<br>

![4](https://user-images.githubusercontent.com/26208598/70807517-9ab41280-1db5-11ea-9887-b7540d97b85b.PNG)

 
### Manage User
#### `/user/my_account/`

![5](https://user-images.githubusercontent.com/26208598/70807521-9be53f80-1db5-11ea-8d39-2daebf1c7e3e.PNG)


<br>
<br>





-----------------

## Django REST Endpoints

#### Navigation
##### `/api/`

![6](https://user-images.githubusercontent.com/26208598/70807623-d5b64600-1db5-11ea-8430-dcc6a680bf80.PNG)

<br>
<br>

#### User
##### `api/user/**`

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


##### Web Development:
Django | Django RESTful | Vue.js | Heroku | Bootstrap | Materialize | AWS S3

##### Database Development:
Postgres | SQLite

##### Python & JS – data analysis & visualisation:
pandas | numpy | scikit-learn | vuechart.js

##### Testing
Django.test

##### LinkedIn API with Python 
https://github.com/ozgur/python-linkedin

<br>
<br>

##### Thank you,

Lukasz Malucha
