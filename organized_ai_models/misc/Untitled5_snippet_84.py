import requests

# Replace 'YOUR_NGROK_URL' with the actual Ngrok URL provided when Flask is running
ngrok_url = "https://6e05-34-138-79-32.ngrok-free.app"  # Use your current Ngrok URL

# Sample endpoint to test user addition
response = requests.post(f"{ngrok_url}/add_user", json={
    "username": "test_user",
    "email": "test@example.com"
})

# Print the raw response content to see what the server returned
print("Raw Response Content:", response.text)

# Attempt to decode the response as JSON if possible
try:
    print("Add User Response:", response.json())
except requests.JSONDecodeError:
    print("Response is not in JSON format.")
