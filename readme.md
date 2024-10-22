Budget Manager

A Django-based API to manage income and expenses, providing users with a summary of their financial status. This project includes JWT-based authentication, API for tracking income and expenses, and functionality to export reports to Excel.
Features

    User Authentication: JWT-based authentication for secure access.
    Income/Expense Tracking: Track individual incomes and expenses.
    Summary Report: Get a summary of total income and expenses for each user.
    Excel Export: Export summary reports in Excel format.
    RESTful API: Built using Django REST Framework.

Prerequisites

Before running the project, ensure you have the following installed:

    Python 3.x
    Django 5.1.2
    MySQL (or your chosen database)
    Django REST Framework
    openpyxl library for Excel export

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/budget-manager.git

Navigate into the project directory:

bash

cd budget-manager

Create a virtual environment:

bash

python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install the required dependencies:

bash

pip install -r requirements.txt

Set up environment variables:

    Create a .env file in the project root and add your database credentials and secret key:

bash

SECRET_KEY=your_secret_key
DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

Run migrations:

bash

python manage.py migrate

Create a superuser:

bash

python manage.py createsuperuser

Run the development server:

bash

    python manage.py runserver

API Endpoints

    Authentication:
        POST /api/token/: Obtain JWT token.
        POST /api/token/refresh/: Refresh token.

    Income:
        GET /api/income/: Get all income records.
        POST /api/income-enter/: Create a new income record.
        PUT /api/income-update/{pk}/: Update an existing income record.
        GET /api/income-get/{pk}/: Retrieve a specific income record.
        DELETE /api/income-delete/{pk}/: Delete a specific income record.

    Expense:
        GET /api/Expense/: Get all expense records.
        POST /api/Expense-enter/: Create a new expense record.
        PUT /api/Expense-update/{pk}/: Update an existing expense record.
        GET /api/Expense-get/{pk}/: Retrieve a specific expense record.
        DELETE /api/Expense-delete/{pk}/: Delete a specific expense record.

    Category:
        GET /api/Category/: Get all categories.
        POST /api/Category-enter/: Create a new category.
        PUT /api/Category-update/{pk}/: Update an existing category.
        DELETE /api/Category-delete/{pk}/: Delete a specific category.

    Goal:
        GET /api/goal/: Get all goals.
        POST /api/goal-enter/: Create a new goal.
        PUT /api/goal-update/{pk}/: Update an existing goal.
        GET /api/goal-get/{pk}/: Retrieve a specific goal.
        DELETE /api/goal-delete/{pk}/: Delete a specific goal.

    Summary Report:
        GET /api/report/<user_id>/: Get total income and expenses for a specific user.
Database

The project uses MySQL by default. Configure the database in the .env file:

bash

DB_NAME=your_db_name
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=localhost
DB_PORT=3306

Exporting Reports to Excel

The project supports exporting income and expense summary reports to Excel. The endpoint:

    GET /api/report/{user_id}/: Exports the report for the specified user.

Running Tests

To run tests, use the following command:

bash

python manage.py test

