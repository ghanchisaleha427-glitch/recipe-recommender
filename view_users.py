import sqlite3
import pandas as pd
from tabulate import tabulate

conn = sqlite3.connect("users.db")

# === Users Table ===
print("\n=== Users Table ===")
users = pd.read_sql_query("SELECT * FROM users", conn)
if not users.empty:
    print(tabulate(users, headers="keys", tablefmt="grid"))
else:
    print("No users found.")

# === User Activity Table ===
print("\n=== User Activity Table ===")
activity = pd.read_sql_query("""
    SELECT ua.id, u.username, ua.user_email, ua.recipe_id, ua.recipe_name, ua.image_url, ua.action, ua.timestamp
    FROM user_activity ua
    LEFT JOIN users u ON ua.user_email = u.email
""", conn)
if not activity.empty:
    print(tabulate(activity, headers="keys", tablefmt="grid"))
else:
    print("No activity found.")

# === Feedback Table ===
print("\n=== Feedback Table ===")
feedback = pd.read_sql_query("SELECT * FROM feedback", conn)
if not feedback.empty:
    print(tabulate(feedback, headers="keys", tablefmt="grid"))
else:
    print("No feedback found.")

conn.close()
