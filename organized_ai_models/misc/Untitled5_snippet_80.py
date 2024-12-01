# Install necessary packages
!pip install firebase-admin flask pyngrok

import os
import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from pyngrok import ngrok

# Firebase Admin setup - automatically initializes if not already done
if not firebase_admin._apps:
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Ensure path is correct
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Cultra Interactive Platform API is running!"

@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        username = data['username']
        email = data['email']

        # Create or update the user in Firestore
        user_data = {
            "username": username,
            "email": email,
            "interaction_count": 0
        }
        db.collection('users').document(username).set(user_data)

        return jsonify({"status": "success", "data": user_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    try:
        user_ref = db.collection('users').document(username)
        user_doc = user_ref.get()

        if user_doc.exists:
            return jsonify({"status": "success", "data": user_doc.to_dict()}), 200
        else:
            return jsonify({"status": "error", "message": "User not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# Start Ngrok tunnel
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Run the Flask app
app.run(port=5000)
