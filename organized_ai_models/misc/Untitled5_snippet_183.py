# Import necessary libraries
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from pyngrok import ngrok
import requests

# Path to your Firebase service account key
service_account_path = "/content/drive/My Drive/BrandNewKey.json"

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Create Flask app
app = Flask(__name__)

# Define /add_user endpoint
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get("username")
    email = data.get("email")

    if not username or not email:
        return jsonify({"status": "error", "message": "Missing username or email"}), 400

    # Add user to Firestore
    user_ref = db.collection("users").document(username)
    user_ref.set({
        "username": username,
        "email": email,
        "interaction_count": 0
    })

    # Return success response
    return jsonify({"status": "success", "data": data}), 200

# Start Ngrok tunnel
public_url = ngrok.connect(5000)
print("Ngrok Tunnel URL:", public_url)

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
