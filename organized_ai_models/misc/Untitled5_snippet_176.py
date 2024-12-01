from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
import os

# Initialize Firebase Admin with your service account key
cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Adjust the path if necessary
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Initialize Flask app
app = Flask(__name__)

# Endpoint to register a new user
@app.route('/register_user', methods=['POST'])
def register_user():
    data = request.json
    user_id = data.get("user_id")
    user_data = data.get("user_data")
    db.collection('users').document(user_id).set(user_data)
    return jsonify({"status": "User registered successfully"}), 200

# Endpoint to log interaction
@app.route('/log_interaction', methods=['POST'])
def log_interaction():
    data = request.json
    interaction_id = data.get("interaction_id")
    interaction_data = data.get("interaction_data")
    db.collection('interactions').document(interaction_id).set(interaction_data)
    return jsonify({"status": "Interaction logged successfully"}), 200

# Endpoint for adaptive response based on user data
@app.route('/adaptive_response', methods=['POST'])
def adaptive_response():
    data = request.json
    user_id = data.get("user_id")
    response_data = data.get("response_data")
    db.collection('responses').document(user_id).set(response_data)
    return jsonify({"status": "Adaptive response recorded"}), 200

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
