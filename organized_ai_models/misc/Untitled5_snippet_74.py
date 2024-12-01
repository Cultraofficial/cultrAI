# Import necessary packages
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
import pyngrok.ngrok as ngrok
import os

# Initialize Flask app
app = Flask(__name__)

# Firebase setup - automatically initializes if not already done
if not firebase_admin._apps:
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Update path if necessary
    initialize_app(cred)
db = firestore.client()

# Define a route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    try:
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        user_data = {
            "username": username,
            "email": email,
            "interaction_count": 0
        }
        db.collection('users').document(username).set(user_data)
        return jsonify({"status": "success", "data": user_data}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Define a route to get a user
@app.route('/get_user/<username>', methods=['GET'])
def get_user(username):
    try:
        user = db.collection('users').document(username).get()
        if user.exists:
            return jsonify({"status": "success", "data": user.to_dict()}), 200
        else:
            return jsonify({"status": "error", "message": "User not found"}), 404
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# Start the Flask app and Ngrok tunnel
if __name__ == '__main__':
    # Set up Ngrok tunnel
    public_url = ngrok.connect(5000)
    print(f"Public URL: {public_url}")

    # Run the Flask app
    app.run()
