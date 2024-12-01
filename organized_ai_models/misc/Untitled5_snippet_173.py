# Install necessary libraries if not already installed
!pip install flask pyngrok firebase-admin

# Import libraries
from flask import Flask, request, jsonify
from pyngrok import ngrok
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin with your service account key
cred = credentials.Certificate("/content/drive/My Drive/BrandNewKey.json")  # Adjust path if necessary
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return "Cultra Interactive Platform API is running!"

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    db.collection('users').document(data['user_id']).set(data)
    return jsonify({"status": "User added"}), 201

@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    user = db.collection('users').document(user_id).get()
    if user.exists:
        return jsonify(user.to_dict()), 200
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/update_user/<user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    db.collection('users').document(user_id).update(data)
    return jsonify({"status": "User updated"}), 200

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    db.collection('users').document(user_id).delete()
    return jsonify({"status": "User deleted"}), 200

# Start ngrok and expose the Flask app
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Start the Flask app
app.run(port=5000)
