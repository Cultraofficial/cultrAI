import os
import requests
from firebase_admin import credentials, initialize_app, firestore
from flask import Flask, request, jsonify
from pyngrok import ngrok

# Firebase Initialization
if not firebase_admin._apps:
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Adjust the path if necessary
    initialize_app(cred)
db = firestore.client()

# Flask app initialization
app = Flask(__name__)

# Automatically create a new Ngrok tunnel if needed
ngrok_tunnel = ngrok.connect(5000)
ngrok_url = ngrok_tunnel.public_url
print(f"Public URL: {ngrok_url}")

@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        user_data = request.get_json()
        username = user_data["username"]
        email = user_data["email"]

        # Store user in Firestore
        db.collection("users").document(username).set({
            "username": username,
            "email": email,
            "interaction_count": 0
        })

        return jsonify({"status": "success", "data": user_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Run Flask app
app.run()

# Testing user addition automatically with Ngrok URL
try:
    response = requests.post(f"{ngrok_url}/add_user", json={
        "username": "test_user",
        "email": "test@example.com"
    })
    print("Add User Response:", response.json())
except requests.JSONDecodeError:
    print("Response is not in JSON format.")
