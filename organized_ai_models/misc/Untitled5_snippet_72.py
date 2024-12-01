# Import necessary libraries
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import os
from google.cloud import storage

# Initialize Flask app
app = Flask(__name__)

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Adjust path as needed
initialize_app(cred)
db = firestore.client()

# Endpoint to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.json
        username = data['username']
        email = data['email']
        user_data = {
            'username': username,
            'email': email,
            'interaction_count': 0
        }
        db.collection('users').document(username).set(user_data)
        return jsonify({'status': 'success', 'data': user_data}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Endpoint to retrieve a user
@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    try:
        user = db.collection('users').document(username).get()
        if user.exists:
            return jsonify({'status': 'success', 'data': user.to_dict()}), 200
        else:
            return jsonify({'status': 'error', 'message': 'User not found'}), 404
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

# Start Flask app with Ngrok tunnel
from pyngrok import ngrok
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Run the app
app.run(port=5000)
