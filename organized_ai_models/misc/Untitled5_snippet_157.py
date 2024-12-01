# Install Flask if not already installed
!pip install Flask pyngrok firebase-admin

import firebase_admin
from firebase_admin import credentials, firestore
from flask import Flask, jsonify, request
import threading
from pyngrok import ngrok

# Initialize Firebase
cred = credentials.Certificate("/content/drive/My Drive/BrandNewKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()

# Initialize Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Interactive Platform!"})

@app.route('/interaction', methods=['POST'])
def interaction():
    # Placeholder for processing viewer input
    data = request.json
    response = {"message": "Received viewer input", "input": data}
    return jsonify(response)

# Run Flask app in a separate thread
def run_flask():
    app.run(port=5000)

flask_thread = threading.Thread(target=run_flask)
flask_thread.start()

# Start Ngrok tunnel to expose the app
public_url = ngrok.connect(5000)
print(f"Public URL: {public_url}")
