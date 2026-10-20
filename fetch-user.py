import requests

url = "https://jsonplaceholder.typicode.com/users/4"
response = requests.get(url, timeout=10)

print("Status:", response.status_code)
user = response.json()
print("Name:", user["name"])
print("Email:", user["email"])
print("City:", user["address"]["city"])