# Canary Homework

The repo contains both two codebases,

  

## Set up database

1. install postgres

   `brew install postgresql`

2. Create postgres db user

   `CREATE USER canary WITH PASSWORD 'c4n4ry'`

3. create tablespace

​	`CREATE TABLESPACE canaryspace OWNER canary LOCATION '/Users/rajibsingh/dbs/canaryspace';`

4. Create db and link to user and tablespace

​	`CREATE DATABASE canarydb OWNER canary TABLESPACE canaryspace;`

5. Verify connection to the database is working

   `psql -h localhost -U canary -d canarydb`



## Django Config

### Set up Python runtime virtual environment

1. Install virtualenv

   `pip install virtualenv`

2. Create canary environment

​	`virtualenv canaryenv`

3. Activate environment

​	`source canaryenv/bin/activate`

4. Install django and all the dependencies

   `pip install -r requirements.txt`

5. Test django is installed

​	`django-admin --version`

6. examine the sample.env and replace the GITHUB_CLIENT_ID and the GITHUB_CLIENT_SECRET with correct entries for your github account. Once this is done, rename the file to .env so that the application will be able to read it

7. Install postgres connectivity library

​	`pip install psycopg2-binary`

8. Run local dev server

​	`python manage.py runserver`

9. Set up a super-user

​	`python manage.py createsuperuser --username=raj --email=rajibsingh@gmail.com`



## VUE Setup

### Set up Vue

1. v22.9.0 (npm v10.8.3)
2. go to canary_vue project
3. run by typing `npm run dev` and the server will run at http://localhost:5173/



### Register OAuth Application

Homepage: http://127.0.0.1:8000

Auth callback URL: http://127.0.0.1:8000/gh_connect/callback/

Device Flow does not need to be enabled

Client ID: 

`Ov23li4yCojB4jPOyIwJ`

Client Secret:  

l
