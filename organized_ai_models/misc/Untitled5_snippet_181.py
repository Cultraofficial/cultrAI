import requests
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from flask import Flask, request, jsonify
from pyngrok import ngrok
import json

# Firebase Initialization - Automatically applies if not already done
if not firebase_admin._apps:
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Adjust path if necessary
    initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# Flask App
app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")
    interaction_count = 0

    user_data = {
        "username": username,
        "email": email,
        "interaction_count": interaction_count
    }
    db.collection("users").document(username).set(user_data)
    return jsonify({"status": "success", "data": user_data}), 200

# Start Flask Server with Ngrok
port = 5000
ngrok_tunnel = ngrok.connect(port)
print("Ngrok Tunnel URL:", ngrok_tunnel.public_url)
app.run(port=port)

# Automatically Test Endpoint
try:
    # Making the request to the new ngrok URL automatically
    response = requests.post(f"{ngrok_tunnel.public_url}/add_user", json={
        "username": "sacrifice in cultra",
        "email": "sacrifice@example.com"
    })

    # Print the response
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except requests.exceptions.RequestException as e:
    print("Request failed:", e)
except json.JSONDecodeError:
    print("Response is not in JSON format. Raw Response Content:", response.content)
