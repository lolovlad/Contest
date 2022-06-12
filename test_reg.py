import requests

'''data = {
    "login": "admin",
    "password": "admin",
    "type": 1,
    "name": "Vlad",
    "sename": "Skripnik",
    "secondname": "Vicktor"
}


BASE = "http://127.0.0.1:5000"
response = requests.post(f"{BASE}/users/0", data)
response = response.json()
if response.get("error") is None:
    print("ok")
else:
    print(response["error"])'''


data = {
    "login": "admin",
    "password": "admin",
    "type": 1,
    "name": "Vlad",
    "sename": "Skripnik",
    "secondname": "Vicktor"
}


BASE = "http://127.0.0.1:5000"
response = requests.post(f"{BASE}/users/0", data)
response = response.json()
if response.get("error") is None:
    print("ok")
else:
    print(response["error"])

