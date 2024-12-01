import requests

url = "https://516c-34-138-79-32.ngrok-free.app/add_user"
data = {
    "username": "test_user",
    "email": "test@example.com"
}

response = requests.post(url, json=data)
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
