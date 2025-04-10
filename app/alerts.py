from database import get_db
from models import Expense, Budget

def check_budget(user_id, category):
    db = next(get_db())
    budget = db.query(Budget).filter_by(user_id=user_id, category=category).first()
    total_spent = sum(exp.amount for exp in db.query(Expense).filter_by(user_id=user_id, category=category).all())

    if budget and total_spent >= budget.amount * 0.9:
        return f"Warning! You have used 90% of your budget for {category}!"
    return "You're within budget."
