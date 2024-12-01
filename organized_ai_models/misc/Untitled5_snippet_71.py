import firebase_admin
from firebase_admin import credentials, firestore
import os
import requests
from flask import Flask, request, jsonify
from google.cloud import storage
from pyngrok import ngrok

# Initialize Firebase Admin
cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# Initialize Flask app
app = Flask(__name__)

# Automatic Ngrok URL setup
def get_ngrok_url():
    tunnels = ngrok.get_tunnels()
    public_url = [tunnel.public_url for tunnel in tunnels if tunnel.name == 'http']
    if public_url:
        return public_url[0]
    return None

# Endpoint to add a user to Firestore
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    interaction_count = data.get('interaction_count', 0)

    user_data = {
        'username': username,
        'email': email,
        'interaction_count': interaction_count
    }

    # Automatically add to Firestore without manual intervention
    db.collection('users').document(username).set(user_data)
    return jsonify({'status': 'success', 'data': user_data})

# Automatically upload files to Google Cloud Storage
def upload_to_gcs(local_folder, gcs_folder):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket('cultra_official')
    for root, dirs, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            blob = bucket.blob(f"{gcs_folder}/{file_name}")
            blob.upload_from_filename(local_path)
            print(f"Uploaded {file_name} to {gcs_folder}/{file_name}")

# Start the Flask app with automatic Ngrok URL application
if __name__ == '__main__':
    # Create Ngrok tunnel and retrieve public URL
    public_url = ngrok.connect(5000, bind_tls=True)
    print(f"Public URL: {public_url}")

    # Run the Flask app
    app.run(port=5000, host='0.0.0.0')
