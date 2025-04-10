import unittest
from database import get_db
from models import Expense

class ExpenseTrackerTests(unittest.TestCase):

    def test_add_expense(self):
        db = next(get_db())
        new_expense = Expense(user_id=1, category="Food", amount=500, date="2025-04-10")
        db.add(new_expense)
        db.commit()
        self.assertEqual(new_expense.amount, 500)

if __name__ == "__main__":
    unittest.main()
