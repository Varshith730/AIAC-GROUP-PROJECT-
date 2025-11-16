# app_safe.py
from flask import Flask, request
import sqlite3
import os
import uuid
from werkzeug.utils import secure_filename
import hmac

app = Flask(__name__)
DB = 'test_safe.db'
UPLOAD_DIR = './uploads_safe'
os.makedirs(UPLOAD_DIR, exist_ok=True)

ALLOWED_EXT = {'txt', 'png', 'jpg', 'jpeg', 'pdf'}

def get_db():
    conn = sqlite3.connect(DB)
    return conn

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXT

@app.route('/')
def index():
    return '<h2>AI-Patched Safe App</h2><ul><li><a href="/login">Login</a></li><li><a href="/upload">Upload</a></li></ul>'

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        conn = get_db()
        cur = conn.cursor()

        # ✅ SAFE: parameterized query avoids SQL injection
        cur.execute("SELECT id, password FROM users WHERE username = ?", (username,))
        row = cur.fetchone()

        if row:
            stored_pass = row[1] or ""
            # constant-time compare
            if hmac.compare_digest(stored_pass, password):
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
        f = request.files.get('file')
        if not f:
            return "No file provided", 400

        filename = secure_filename(f.filename)

        if not filename or not allowed_file(filename):
            return "Invalid file type", 400

        # randomize filename to avoid collisions
        saved_name = uuid.uuid4().hex + "_" + filename
        filepath = os.path.join(UPLOAD_DIR, saved_name)
        f.save(filepath)

        return "Uploaded safely: %s" % filepath

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
