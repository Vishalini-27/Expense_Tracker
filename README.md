# Expense_Tracker

## Overview
This is a Python **Expense Tracker** program that allows users to:
- Record daily expenditure.
- Categorize costs.
- Make monthly budgets for various categories.
- Receive **notifications when budget limits are exceeded**.
- Look at **category spending reports**.

It is built with **Flask, SQLAlchemy, SQLite/PostgreSQL**, and supports **Docker-based deployment**.

## **1️.Prerequisites**
Before installing the program, ensure that you have
- Python **3.10+** installed.
- **Flask** and **SQLAlchemy** installed (see below dependencies). - Docker installed (optional, for containerized deployment).

---

## **2️.Installation Guide**

To download and run the application, do the following: 

### Step 1: Clone the Repository
### Step 2: Create Virtual Environment
python -m venv venv source venv/bin/activate  # MacOS/Linux 
venv\Scripts\activate     # Windows

### Step 3: Install Dependencies
pip install -r requirements.txt

### Step 4: Initialize the Database
python -c "from database import engine, Base; Base.metadata.create_all(engine)"

This sets up the necessary tables for users, expenses, and budgets.
### Step 5: Run the Application
python run.py
Your server should start at: **http://127.0.0.1:5000/**

## **3️.Docker Deployment**
To build and run the application using Docker, follow these steps:

### Step 1: Build the Docker Image
docker build -t expense-tracker .

### Step 2: Run the Application in a Container
docker run -p 5000:5000 expense-tracker

## **4️.API Endpoints**
The application exposes several REST API endpoints:

### **1. Add Expense**
**POST** `/add_expense`
- Request Body:
  { "user_id": 1, "category": "Food", "amount": 500, "date": "2025-04-10" }
- Response:
  {"message": "Expense added successfully!"}

### **2. Get Expenses**
**GET** `/get_expenses?user_id=1`
- Returns all expenses for a given user.

### **3. Set Monthly Budget**
**POST** `/set_budget`
- Request Body:
  { "user_id": 1, "category": "Transport", "amount": 3000 }
- Response:
  {"message": "Budget set successfully!"}
  
### **4. Check Budget Usage**
**GET** `/check_budget?user_id=1&category=Food`
- Returns spending details against the budget.


## **5️.Running Tests**
To verify the functionality, run the unit tests:
python -m unittest discover tests


## **6️.Edge Case Handling**
The application is designed to handle:
- Invalid expense entries (negative amounts).
- Missing fields in API requests.
- Budget alerts when **90% of the budget is consumed**.
- Handling expense sharing logic.

## **7️.Future Enhancements**
Enhancements that could be implemented:
- **User authentication** for secure expense logging.
- **Graphical dashboard** for better insights into spending trends.
- **Expense-sharing feature** for tracking group expenses.

## **8️.Technologies Used**
- **Backend:** Python (Flask), SQLAlchemy
- **Database:** SQLite/PostgreSQL
- **Containerization:** Docker
- **Alerts:** Email Notifications via SMTP

## **9️.Maintainers**
Maintained by Vishalini P. 


  


