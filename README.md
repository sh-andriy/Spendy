# Spendy
 Expenses Tracker App

### Follow this link to access hosted web-service:
```terminal
spendy-westcoast.herokuapp.com
```

<hr/>

## To set up a project follow this steps:
### 1. Clone repo:
```terminal
git clone https://github.com/sh-andriy/Spendy.git
```
<br>

### 2. Activate virtual environment:
```shell
virtualenv venv
```
```shell
source env/bin/activate
```
<br>

### 3. Install pip and upgrade it:
```shell
python -m ensurepip
```
#### or
```shell
python3 -m ensurepip
```
#### ugrade
```shell
python3 -m pip install –upgrade pip
```
<br>

### 4. Install all the project dependencies:
```shell
pip install -r requirements.txt
```
#### or
```shell
pip install .
```
<br>

## Configure Database:
<hr>

### 5. Set these environmental variables in .env file:
```shell
DB_HOST=<host>
DB_USERNAME=<username>
DB_PASSWORD=<password>
SECRET_KEY=<something>
```

### 6. Run migrations:

- `python manage.py makemigrations`
- `python manage.py migrate`

### Run server:
```shell
python manage.py runserver
```

## Congrats! You've gained access to the following:
<hr>