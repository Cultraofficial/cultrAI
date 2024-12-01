import requests

# Replace with the current Ngrok URL
ngrok_url = "https://12e0-34-138-79-32.ngrok-free.app/add_user"

# Sample user data
user_data = {
    "username": "test_user",
    "email": "test@example.com"
}

response = requests.post(ngrok_url, json=user_data)

# Print the response status and raw content
print("Status Code:", response.status_code)
print("Raw Response Content:", response.text)

# Try parsing as JSON only if the response is expected to be in JSON format
try:
    json_response = response.json()
    print("JSON Response:", json_response)
except requests.exceptions.JSONDecodeError:
    print("Response is not in JSON format.")
