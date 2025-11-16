# app_vulnerable.py
from flask import Flask, request
import sqlite3
import os

app = Flask(__name__)
DB = 'test_vuln.db'
UPLOAD_DIR = './uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

def get_db():
    conn = sqlite3.connect(DB)
    return conn

@app.route('/')
def index():
    return '<h2>AI-Generated Vulnerable App</h2><ul><li><a href="/login">Login</a></li><li><a href="/upload">Upload</a></li></ul>'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # ❌ VULNERABLE: SQL Injection via string formatting
        query = "SELECT id FROM users WHERE username = '%s' AND password = '%s'" % (username, password)

        conn = get_db()
        cur = conn.cursor()
        cur.execute(query)
        row = cur.fetchone()

        if row:
            return "Logged in as user %s" % username
        return "Login failed"

    return '''
      <form method="post">
        username: <input name="username"><br>
        password: <input name="password"><br>
        <input type="submit">
      </form>
    '''

@app.route('/upload', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        # ❌ VULNERABLE: uses filename directly → allows path traversal
        filepath = os.path.join(UPLOAD_DIR, f.filename)
        f.save(filepath)

        return "Uploaded: %s" % filepath

    return '''
      <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit">
      </form>
    '''

if __name__ == '__main__':
    conn = sqlite3.connect(DB)
    conn.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)')
    conn.execute("INSERT OR IGNORE INTO users (id, username, password) VALUES (1, 'admin', 'adminpass')")
    conn.commit()
    conn.close()
    app.run(debug=True)
