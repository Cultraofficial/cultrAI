from flask import Flask, jsonify, request
from pyngrok import ngrok
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Flask app
app = Flask(__name__)

# Firebase setup - automatically initializes if not already done
if not firebase_admin._apps:
    cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Update path if necessary
    firebase_admin.initialize_app(cred)

# Firestore client setup
db = firestore.client()

# Start Ngrok tunnel
public_url = ngrok.connect(5000)
print("Ngrok Tunnel URL:", public_url)

# Define route to add a user
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')

    user_data = {
        "username": username,
        "email": email,
        "interaction_count": 0
    }
    db.collection('users').document(username).set(user_data)
    return jsonify({"status": "success", "data": user_data})

if __name__ == '__main__':
    app.run(port=5000)
