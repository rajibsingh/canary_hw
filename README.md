# Canary Homework

The repo contains both two codebases,

  

## Set up database

1. Create postgres db user

   `CREATE USER canary WITH PASSWORD 'c4n4ry'`

2. create tablespace

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

6. examine the sample.env and replace the GITHUB_CLIENT_ID, GITHUB_CLIENT_SECRET and WEBHOOK_SECRET_TOKEN with correct entries for your github account. Once this is done, rename the file to .env so that the application will be able to read it

8. Run local dev server

​	`python manage.py runserver`

9. Set up a super-user

​	`python manage.py createsuperuser --username=<your username> --email=<your email address>`

​	you will be asked to set the user password through the console

10. Copy sample.env file into a new file called .env and update requested parameters



## VUE Setup

### Set up Vue

1. install nvm, refer to nvm
2. set nvm to use the current stable version, currently as v22.9.0 (npm v10.8.3)

​	`nvm use stable`

3. download dependencies

​	`npm install`

4. Copy sample.env into .env and update with requested parameters
5. run the server by typing `npm run dev`. The server will be available at http://localhost:5173/



