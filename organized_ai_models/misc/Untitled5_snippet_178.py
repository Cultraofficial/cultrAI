import os  # Add this import
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud import storage

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

# Google Cloud Storage upload function
BUCKET_NAME = 'cultra_official'
storage_client = storage.Client()
bucket = storage_client.bucket(BUCKET_NAME)

def upload_to_gcs(local_folder, gcs_folder):
    for root, dirs, files in os.walk(local_folder):
        for file_name in files:
            local_path = os.path.join(root, file_name)
            gcs_path = os.path.join(gcs_folder, file_name)
            blob = bucket.blob(gcs_path)
            blob.upload_from_filename(local_path)
            print(f"Uploaded {local_path} to {gcs_path} in GCS")

# Example usage
upload_to_gcs('platform', 'platform')  # Upload platform files
upload_to_gcs('data', 'data')          # Upload data files
upload_to_gcs('models', 'models')      # Upload model files

# Run the Flask app
if __name__ == '__main__':
    app.run(port=5000)
