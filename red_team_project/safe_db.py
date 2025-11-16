# safe_db.py (snippet)
cur.execute("SELECT id FROM users WHERE username = ? AND password = ?", (username, password))
