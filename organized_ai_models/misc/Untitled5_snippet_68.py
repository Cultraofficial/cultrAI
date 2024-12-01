# Flask app with endpoints for expanded functionality
from flask import Flask, request, jsonify
from firebase_admin import credentials, firestore, initialize_app
import firebase_admin

# Initialize Firebase
if not firebase_admin._apps:
    cred = credentials.Certificate("/content/drive/My Drive/BrandNewKey.json")
    initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

# Endpoint to add user
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
    return jsonify({'status': 'success', 'data': user_data}), 200

# Endpoint to track interactions
@app.route('/track_interaction', methods=['POST'])
def track_interaction():
    data = request.get_json()
    username = data.get('username')
    user_ref = db.collection('users').document(username)
    user = user_ref.get()
    if user.exists:
        new_count = user.to_dict().get('interaction_count', 0) + 1
        user_ref.update({'interaction_count': new_count})
        return jsonify({'status': 'success', 'interaction_count': new_count}), 200
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

# Endpoint to retrieve user data
@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    user_ref = db.collection('users').document(username)
    user = user_ref.get()
    if user.exists:
        return jsonify({'status': 'success', 'data': user.to_dict()}), 200
    else:
        return jsonify({'status': 'error', 'message': 'User not found'}), 404

# Endpoint to fetch all users (useful for testing and analytics)
@app.route('/all_users', methods=['GET'])
def all_users():
    users = [doc.to_dict() for doc in db.collection('users').stream()]
    return jsonify({'status': 'success', 'data': users}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
