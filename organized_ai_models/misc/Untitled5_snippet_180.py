import requests

# Replace with the latest ngrok URL
ngrok_url = "https://fdee-34-138-79-32.ngrok-free.app"  # Update this with the current ngrok URL if it changes

# Test adding a new user with the name "sacrifice in cultra"
response = requests.post(f"{ngrok_url}/add_user", json={
    "username": "sacrifice in cultra",
    "email": "sacrifice@example.com"
})

# Print the response
print("Status Code:", response.status_code)
try:
    print("Response JSON:", response.json())
except ValueError:
    print("Response is not in JSON format. Raw Response Content:", response.content)
