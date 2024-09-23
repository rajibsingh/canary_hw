# Canary Homework



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



## Set up Python runtime virtual environment

1. Install virtualenv

   `pip install virtualenv`

2. Create canary environment

​	`virtualenv canaryenv`

3. Activate environment

​	`source canaryenv/bin/activate`

4. Install django

   `pip install django`

5. Test django is installed

​	`django-admin --version`



## Configure Django

1. Install postgres connectivity library

​	`pip install psycopg2-binary`

2. Run local dev server

​	`python manage.py runserver`

3. Set up a super-user

   `python manage.py createsuperuser --username=raj --email=rajibsingh@gmail.com`



## Set up Vue

1. go to canary_vue project
2. run by typing `npm run dev` and the server will run at http://localhost:5173/







