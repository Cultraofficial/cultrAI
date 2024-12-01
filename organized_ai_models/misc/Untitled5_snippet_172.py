import requests

# Define the base URL for your local server (via ngrok if needed)
base_url = "http://127.0.0.1:5000"  # Replace with your public ngrok URL if using ngrok

# 1. Add a User
def add_user(user_id, name, email):
    response = requests.post(f"{base_url}/add_user", json={
        "user_id": user_id,
        "name": name,
        "email": email
    })
    return response.json()

# 2. Get a User
def get_user(user_id):
    response = requests.get(f"{base_url}/get_user/{user_id}")
    return response.json()

# 3. Update a User
def update_user(user_id, interactions):
    response = requests.patch(f"{base_url}/update_user/{user_id}", json={
        "interactions": interactions
    })
    return response.json()

# 4. Delete a User
def delete_user(user_id):
    response = requests.delete(f"{base_url}/delete_user/{user_id}")
    return response.json()

# Testing the functions
# Add a user
print("Adding user:")
print(add_user("user_001", "John Doe", "johndoe@example.com"))

# Get the user's information
print("\nGetting user information:")
print(get_user("user_001"))

# Update the user's interactions
print("\nUpdating user interactions:")
print(update_user("user_001", [{"scene_id": "scene_1", "choice": "Go left"}]))

# Delete the user
print("\nDeleting user:")
print(delete_user("user_001"))
