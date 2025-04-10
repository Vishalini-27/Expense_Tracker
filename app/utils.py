import smtplib
from email.mime.text import MIMEText
from database import get_db
from models import Expense, Budget
from datetime import datetime

def format_currency(amount):
    """Format a number as currency (₹ or $ based on preference)."""
    return f"₹{amount:.2f}"

def get_total_spending(user_id, month):
    """Calculate total spending for a given month."""
    db = next(get_db())
    expenses = db.query(Expense).filter(Expense.user_id == user_id, Expense.date.like(f"{month}-%")).all()
    return sum(exp.amount for exp in expenses)

def send_email_alert(recipient_email, subject, message):
    """Send budget alerts via email."""
    sender_email = "your_email@example.com"  
    password = "your_email_password"  
    
    msg = MIMEText(message)
    msg["Subject"] = subject
    msg["From"] = sender_email
    msg["To"] = recipient_email

    try:
        server = smtplib.SMTP_SSL("smtp.example.com", 465)  
        server.login(sender_email, password)
        server.sendmail(sender_email, [recipient_email], msg.as_string())
        server.quit()
        print("Email alert sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")
