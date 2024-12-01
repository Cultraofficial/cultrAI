# Install necessary packages (if not already installed)
!pip install flask firebase-admin pyngrok requests

import json
import requests
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
from pyngrok import ngrok

# Firebase Initialization
try:
    if not initialize_app._apps:
        cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Ensure this path is correct
        initialize_app(cred)
    db = firestore.client()
except Exception as e:
    print(f"Error initializing Firebase: {e}")

# Flask Application Setup
app = Flask(__name__)

# Define the /add_user endpoint
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data or 'username' not in data or 'email' not in data:
        return jsonify({'error': 'Invalid input'}), 400

    username = data['username']
    email = data['email']

    # Add user to Firestore
    try:
        user_ref = db.collection('users').document(username)
        user_ref.set({
            'username': username,
            'email': email,
            'interaction_count': 0
        })
        return jsonify({'status': 'success', 'data': data}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Run Flask with Ngrok
public_url = ngrok.connect(5000)
print("Ngrok Tunnel URL:", public_url)

app.run(port=5000)
