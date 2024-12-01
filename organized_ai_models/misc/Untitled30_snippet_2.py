import requests

# Replace with your actual Nhost backend URL
backend_url = "https://backend-f15f29b1-336c-4159-b89f-50a835eafa6e.nhost.run/v1/graphql"

# Optional: Add an authentication token if required
auth_token = "your_auth_token"  # Replace with a valid token if your project requires it
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {auth_token}" if auth_token else None
}
