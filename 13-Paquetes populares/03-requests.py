import requests
import os

urlbase = "https://jsonplaceholder.typicode.com/users"
# La API key debería estar en variables de entorno
headers = {
    "Content-Type": "application/json",
}

response = requests.get(urlbase, timeout=10)
print(response.status_code)
print(response.json())

users = response.json()
for user in users:
    print(f"Nombre: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Teléfono: {user['phone']}")
    print(
        f"Dirección: {user['address']['street']}, {user['address']['suite']}, {user['address']['city']}, {user['address']['zipcode']}")
    print(f"Compañía: {user['company']['name']}")
    print("-" * 40)

response = requests.post(urlbase, headers=headers, json={"name": "John Doe"})
print(response.status_code)
