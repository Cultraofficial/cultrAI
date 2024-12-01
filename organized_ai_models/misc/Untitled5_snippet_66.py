import threading
import requests
from flask import Flask, request, jsonify
from google.cloud import firestore
from pyngrok import ngrok
import time

# Initialize Firestore
db = firestore.Client()

# Flask app setup
app = Flask(__name__)

# Flask routes
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
    db.collection('users').document(username).set(user_data)
    return jsonify({"status": "success", "data": user_data}), 200

@app.route('/update_interaction', methods=['POST'])
def update_interaction():
    data = request.get_json()
    username = data.get('username')
    user_ref = db.collection('users').document(username)
    user = user_ref.get()
    if user.exists:
        user_data = user.to_dict()
        user_data['interaction_count'] += 1
        user_ref.set(user_data)
        return jsonify({"status": "success", "data": user_data}), 200
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    user = db.collection('users').document(username).get()
    if user.exists:
        return jsonify({"status": "success", "data": user.to_dict()}), 200
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

# Function to run Flask app in a thread
def run_flask():
    app.run(port=5000)

# Start ngrok tunnel only once
public_url = ngrok.connect(5000).public_url
print("Public URL:", public_url)

# Run Flask app in a separate thread
threading.Thread(target=run_flask).start()

# Wait a moment to ensure server is ready
time.sleep(3)

# Testing API endpoints
# Test add_user endpoint
response = requests.post(public_url + '/add_user', json={'username': 'test_user', 'email': 'test@example.com'})
print("Add User Response:", response.json())

# Test get_user endpoint
response = requests.get(public_url + '/get_user', params={'username': 'test_user'})
print("Get User Response:", response.json())

# Test update_interaction endpoint
response = requests.post(public_url + '/update_interaction', json={'username': 'test_user'})
print("Update Interaction Response:", response.json())
