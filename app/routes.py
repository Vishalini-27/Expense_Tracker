from flask import Flask, request, jsonify
from database import get_db
from models import Expense, Budget

app = Flask(__name__)

@app.route('/add_expense', methods=['POST'])
def add_expense():
    data = request.json
    db = next(get_db())
    new_expense = Expense(user_id=data['user_id'], category=data['category'], amount=data['amount'], date=data['date'])
    db.add(new_expense)
    db.commit()
    return jsonify({"message": "Expense added successfully!"}), 201
