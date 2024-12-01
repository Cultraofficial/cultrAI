# Install necessary packages if they aren't already installed
!pip install flask pyngrok firebase-admin

# Import libraries
from flask import Flask, request, jsonify
from pyngrok import ngrok
import firebase_admin
from firebase_admin import credentials, firestore
import threading

# Firebase setup
cred = credentials.Certificate("/content/drive/My Drive/BrandNewKey.json")  # Adjust the path to your JSON key file
firebase_admin.initialize_app(cred)
db = firestore.client()

# Flask setup
app = Flask(__name__)

# Define Flask routes
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

# Function to run Flask app
def run_flask():
    app.run(port=5000)

# Start ngrok tunnel
public_url = ngrok.connect(5000)
print("Public URL:", public_url)

# Start Flask in a separate thread
flask_thread = threading.Thread(target=run_flask)
flask_thread.start()
