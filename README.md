# Spendy
 The Financial Expense Tracking Application is a web-based solution that allows users to effectively manage their finances by tracking expenses, incomes, credits, and deposits. The application provides a range of features to ensure seamless financial management and analysis.


### Follow this link to access hosted web-service:
```terminal
spendy-westcoast.herokuapp.com
```

<hr/>

## Key Features

### Transaction Management
Users have complete control and flexibility over their financial data. They can easily add, edit, and delete individual transactions, ensuring accuracy and making adjustments whenever necessary.

### Expense and Income Tracking
The application enables users to log and categorize their expenses and incomes, providing an accurate record of their financial activities. Users can view and analyze their transactions to gain insights into their spending and earning patterns.

### Credit and Deposit Management
Efficiently manage credits and deposits within the application. Users can add new credits or deposits, update existing ones, and effectively track their balances.

### Sorting and Reporting
The project offers sorting capabilities, allowing users to organize transactions based on date, category, or type. Reporting features enable users to generate summaries, charts, or customized reports, empowering them to evaluate their financial performance.

### Secure Editing and Deletion
The application ensures the security and integrity of user data by implementing secure editing and deletion functionalities. Users can modify or remove transactions with confidence, knowing that their financial information is protected.

The project is hosted on Heroku, providing a reliable and scalable platform for seamless user access. It is designed to be fully responsive, allowing users to conveniently manage their financial data from any device.

<hr/>

## Technologies Used

- Django: A Python-based web framework used for backend development.
- HTML/CSS: Used for building the user interface and styling the application.
- JavaScript: Enhances the user experience with interactive elements and dynamic content.
- Heroku: The application is hosted on Heroku for reliable and scalable deployment.
- Privat24 API: The application utilizes the Privat24 API for real-time exchange rate data.

## Getting Started

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

- Please Note that all the urls you can see in `urls.py` files
### Web Service:
```shell
spendy-westcoast.herokuapp.com
spendy-westcoast.herokuapp.com/transactions/
spendy-westcoast.herokuapp.com/users/
spendy-westcoast.herokuapp.com/users/login/
spendy-westcoast.herokuapp.com/users/register/
spendy-westcoast.herokuapp.com/users/logout/
```

### Web Application:
```shell
localhost:8000
localhost:8000/transactions/
localhost:8000/users/
localhost:8000/users/login/
localhost:8000/users/register/
localhost:8000/users/logout/
```
