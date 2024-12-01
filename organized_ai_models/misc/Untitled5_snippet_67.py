import firebase_admin
from firebase_admin import credentials, firestore
import requests
from flask import Flask, request, jsonify
from pyngrok import ngrok
import threading
import time

# Initialize Firebase Admin SDK
try:
    # Load the credentials
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')
    firebase_admin.initialize_app(cred)
    print("Firebase Admin initialized.")
except ValueError as e:
    print("Firebase Admin already initialized.")

# Initialize Firestore
db = firestore.client()

# Flask app setup
app = Flask(__name__)

@app.route('/')
def home():
    return "Cultra Interactive Platform API is running!"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    user_data = {
        'username': username,
        'email': email,
        'interaction_count': 0
    }
    try:
        db.collection('users').document(username).set(user_data)
        return jsonify({"status": "success", "data": user_data}), 200
    except Exception as e:
        print("Error adding user to Firestore:", e)
        return jsonify({"status": "error", "message": str(e)}), 500

# Run Flask app in a separate thread
def run_flask():
    app.run(port=5000)

# Start ngrok tunnel and Flask app
public_url = ngrok.connect(5000).public_url
print("Public URL:", public_url)
threading.Thread(target=run_flask).start()

# Wait to ensure server is ready
time.sleep(3)

# Testing the API
# Test the add_user endpoint
response = requests.post(public_url + '/add_user', json={'username': 'test_user', 'email': 'test@example.com'})
try:
    print("Add User Response:", response.json())
except requests.exceptions.JSONDecodeError:
    print("Failed to decode JSON response from server.")
