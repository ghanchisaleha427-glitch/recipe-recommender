import sqlite3
import bcrypt

def init_db():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT UNIQUE,
            password TEXT
        )
    """)
    # User Activity table (with image_url)
    c.execute("""
        CREATE TABLE IF NOT EXISTS user_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            recipe_id TEXT,
            recipe_name TEXT,
            image_url TEXT,
            action TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    # Feedback table
    c.execute("""
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_email TEXT,
            recipe_id TEXT,
            recipe_name TEXT,
            rating INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()

def add_user(username, email, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    hashed_pw = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    c.execute("INSERT INTO users (username, email, password) VALUES (?, ?, ?)", 
              (username, email, hashed_pw))
    conn.commit()
    conn.close()

def get_user(email):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT username, email, password FROM users WHERE email=?", (email,))
    row = c.fetchone()
    conn.close()
    if row:
        return {"username": row[0], "email": row[1], "password": row[2]}
    return None

def log_activity(user_email, recipe_id, recipe_name, image_url, action):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO user_activity (user_email, recipe_id, recipe_name, image_url, action)
        VALUES (?, ?, ?, ?, ?)
    """, (user_email, recipe_id, recipe_name, image_url, action))
    conn.commit()
    conn.close()

def get_user_activity(user_email):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT recipe_id, recipe_name, image_url, action, timestamp FROM user_activity WHERE user_email=?", (user_email,))
    rows = c.fetchall()
    conn.close()
    return rows

def add_feedback(user_email, recipe_id, recipe_name, rating):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("""
        INSERT INTO feedback (user_email, recipe_id, recipe_name, rating)
        VALUES (?, ?, ?, ?)
    """, (user_email, recipe_id, recipe_name, rating))
    conn.commit()
    conn.close()

def get_feedback(recipe_id="*"):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    if recipe_id == "*":
        c.execute("SELECT user_email, recipe_name, rating, timestamp FROM feedback")
    else:
        c.execute("SELECT user_email, recipe_name, rating, timestamp FROM feedback WHERE recipe_id=?", (recipe_id,))
    rows = c.fetchall()
    conn.close()
    return rows

# Initialize DB
init_db()
