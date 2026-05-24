import sqlite3
import pandas as pd

conn = sqlite3.connect("users.db")

# Users table check
print("=== Users Table ===")
users = pd.read_sql_query("SELECT * FROM users", conn)
if not users.empty:
    print(users.to_string(index=False))
else:
    print("No users found.")

# Activity table check
print("\n=== User Activity Table ===")
activity = pd.read_sql_query("SELECT * FROM user_activity", conn)
if not activity.empty:
    print(activity.to_string(index=False))
else:
    print("No activity found.")

# Feedback table check
print("\n=== Feedback Table ===")
feedback = pd.read_sql_query("SELECT * FROM feedback", conn)
if not feedback.empty:
    print(feedback.to_string(index=False))
else:
    print("No feedback found.")

conn.close()
