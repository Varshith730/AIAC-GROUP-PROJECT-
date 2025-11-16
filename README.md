🛡️ Red Teaming AI-Generated Code — Security Analysis Project

This project performs a Red Team security evaluation on AI-generated Flask backend code to uncover vulnerabilities introduced by insecure coding patterns. The goal is to demonstrate how AI-assisted coding can unintentionally create exploitable weaknesses and to show the importance of reviewing and securing AI-generated code.

🔍 Project Overview

An intentionally vulnerable Flask web application was generated using ChatGPT.
It includes:

A user login system

A file upload feature

Using Red Team techniques, two major vulnerabilities were discovered and exploited:

SQL Injection (SQLi)

File Upload Path Traversal

Proof-of-Concept (PoC) scripts were created to exploit both vulnerabilities.
A secure version of the application was then developed with proper validation, sanitization, and secure database queries.

🧱 Features & Vulnerabilities Tested
✔ SQL Injection (SQLi)

Unsafe SQL query formatting led to authentication bypass

Attack executed using poc_sqli.py

✔ File Upload Path Traversal

User-controlled filenames allowed writing outside upload directory

Exploited using crafted curl.exe request

✔ Secure Version Implemented

Parameterized SQL queries

secure_filename() & UUID-based filenames

File extension validation

Sanitized inputs across routes

📁 Project Structure
├── app_vulnerable.py        # Intentionally insecure Flask application
├── app_safe.py              # Secured, patched version
├── poc_sqli.py              # SQL Injection attack script
├── test.txt                 # Test file for upload exploit
├── screenshots/             # Proof of exploitation
│    ├── login_bypass.png
│    ├── file_traversal.png
├── README.md                # Project documentation

🧪 How to Run the Project Locally
1️⃣ Install dependencies
pip install flask sqlalchemy requests werkzeug

2️⃣ Run the vulnerable Flask application
python app_vulnerable.py


It will run at:
👉 http://127.0.0.1:5000/

3️⃣ Launch SQL Injection attack
python poc_sqli.py

4️⃣ Perform File Upload Path Traversal
curl.exe -v -F "file=@test.txt;filename=../../evil.txt" http://127.0.0.1:5000/upload

🛠️ Tools & Technologies Used

Python 3

Flask Web Framework

SQLite Database

Requests Library (for automated attacks)

curl.exe (for file upload exploit)

Werkzeug (secure_filename)

ChatGPT (OpenAI) for generating the initial code

📌 Key Outcomes

Identified and exploited critical vulnerabilities in AI-generated code.

Developed actionable PoC attack scripts.

Enhanced understanding of secure coding practices.

Produced a secure patched version of the application.

Demonstrated the importance of auditing AI-generated code before deployment.

🚀 Future Enhancements

Add XSS, CSRF, IDOR testing

Implement SAST/DAST tools like Bandit or OWASP ZAP

Add logging & intrusion detection

Extend UI with templates & styling

Create automated security test suite

⚠️ Disclaimer

This project contains intentionally vulnerable code for research and educational purposes only.
Do NOT deploy the vulnerable version on any public server.

👥 Team Members

G. Varshith Raju – 2503A51L02

B. Rajagopal – 2503A51L01

K. Srikar – 2503A51L03

D. Siddhartha – 2503A51L04

SR University – AI Assisted Coding Project
