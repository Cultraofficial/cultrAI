# Import necessary libraries
!pip install firebase-admin flask pyngrok requests

import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, request, jsonify
from pyngrok import ngrok
import requests
import time

# Firebase Initialization
if not firebase_admin._apps:
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Adjust path if necessary
    firebase_admin.initialize_app(cred)
db = firestore.client()

# Flask App Setup
app = Flask(__name__)

# Flask Route for Adding User
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    if username and email:
        # Add user data to Firestore
        user_data = {'username': username, 'email': email, 'interaction_count': 0}
        db.collection('users').document(username).set(user_data)
        return jsonify({'status': 'success', 'data': user_data}), 200
    else:
        return jsonify({'status': 'error', 'message': 'Invalid data'}), 400

# Run Flask App in Background
from threading import Thread
def run_app():
    app.run(port=5000)

flask_thread = Thread(target=run_app)
flask_thread.start()

# Allow time for the Flask server to initialize
time.sleep(3)

# Set up Ngrok tunnel for port 5000 and print public URL
public_url = ngrok.connect(5000).public_url
print(f"Ngrok Tunnel URL: {public_url}")

# Function to Test the Endpoint with Latest Ngrok URL
def test_add_user():
    response = requests.post(f"{public_url}/add_user", json={
        "username": "test_user",
        "email": "test@example.com"
    })
    print("Status Code:", response.status_code)
    try:
        print("Response JSON:", response.json())
    except requests.exceptions.JSONDecodeError:
        print("Response is not in JSON format. Raw Response Content:", response.content)

# Run Test Function
test_add_user()
