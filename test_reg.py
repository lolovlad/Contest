import requests

data = {
    "login": "admin",
    "password": "admin",
    "type": 1,
    "name": "admin",
    "sename": "admin"
}


BASE = "http://127.0.0.1:5000"
response = requests.post(f"{BASE}/registration", data)
response = response.json()
if response.get("error") is None:
    print("ok")
else:
    print(response["error"])

