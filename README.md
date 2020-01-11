# Project Title
>Pizza Order Delivery System 
# Project Description
> EndPoints Api To Allow Users To Do Thier Own Orders Delete Orders Retrive Order And Update Thier Own Orders

# PreeRequsts
 
1.[Postgresql DataBase Server version >= 10](https://www.postgresql.org/download/)

2.[Python version >= 3.6](https://www.python.org)

3.[Python Package Index pip](https://pip.pypa.io/en/stable/)

4.[Git Version Control](https://git-scm.com/)

# Python Used Libraries 

1.[Django](https://djangoproject.com)

2.[Django Rest Framework](https://django-rest-framework.org)


3.[Pipenv Package Manager](https://pipenv-fork.readthedocs.io/en/latest/)

4.[Psycopg2 Postgresql Connector](https://pypi.org/project/psycopg2/)

# How To Run Locally On Your System 

> Please Make Sure That PreeRequsts Installed On Your System To Run This Project Corectly  

1. First Create Db **pizza** On Your Server Localhost Or Remote Server
```
psql --host=localhost --username=postgres --dbname=postgres
```
if you will use remote host use
```
--host={ip for remote host}
```
then you will be prompt for password 
then preform these orders in order to create database pizza
```
create database pizza with encoding="UTF8" owner=postgres;
```
then exit by type 
```
exit 
\q
```
2. second use git to clone project on your system with command
```
git clone https://github.com/BakrFrag/Pizza-Order-System
```
this will clone project and get it on folder called Pizza-Order_System
3.redirect to Project folder *Pizza-Order-System*
```
cd Pizza-Order-System
```
active the virtualenv 
```
pipenv shell
```
install Dependancies Library Used
```
pipenv install 
```
4.redirect to actual Project
```
cd PizaaApp
```
5.To Edit Setting File To Edit Databas Password 
```
cd PizaaApp
```
Edit settings.py file On Database Settings By Replace 

*PASSWORD:With Your Password*

*HOST:With Your Host*

*USER:With Postgresql User*

*Port:Actual Running Port In Your System*

6. applay migrations on database with commands
```
python manage.py makemigrations
python manage.py migrate
```
7. Run The Development Server Of Django By
```
cd ..
python manage.py runserver
```
8. Then Got To Browser And Place
``` 
http://127.0.0.1:8000/pizza/list/api/
```
You Will Find List Of All Orders

# Project Urls Api End Points

1. List All Order Url Get Request 
```
http://127.0.0.1:8000/pizza/list/api/
```
You Can Custimze Result By Using Filters On status And customer Or Poth Of Them Like
```
http://127.0.0.1:8000/pizza/list/api/?status=in_progress&customer=bk
```
replace status with you need and also custome 
you can custimize list by customer only like
```
http://127.0.0.1:8000/pizza/list/api/?customer=bk
```
also you can custimze list by status only
```
http://127.0.0.1:8000/pizza/list/api/?status=in_progress
```
2. Create Order With Post Request 
```
http://127.0.0.1/pizza/create/api/
```
3. update order by Put Request and order ID
```
http://127.0.0.1:8000/pizza/update/api/<int:id>/
```
4. Delete Order By Delete Request And order Id
```
http://127.0.0.1:8000/pizza/delete/api/<int:pk>/
```
5. Retrive Order By Get Request And Order ID 
```
http://127.0.01:8000/pizza/order/<int:pk>/
```

# Test On Project

>There Is 3 Test On tests.py File To Run Them Type 

>Please Read Comments  On tests.py before run it
```
python manage.py test
```
> this will run tests

# Important Notes To Use
> if you run this project in Debian Destributions Like Ubuntu Or Linux Mint Please Install libpq-dev
```
sudo apt-get install libpq-dev
```
> Please Read Comments On Database models , tests , views 
