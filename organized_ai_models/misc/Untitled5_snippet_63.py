from flask import Flask, request, jsonify
from google.cloud import firestore

app = Flask(__name__)
db = firestore.Client()

# Endpoint to add a new user
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

# Endpoint to update user interaction count
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

# Endpoint to retrieve user data
@app.route('/get_user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    user = db.collection('users').document(username).get()
    if user.exists:
        return jsonify({"status": "success", "data": user.to_dict()}), 200
    else:
        return jsonify({"status": "error", "message": "User not found"}), 404

# Run the Flask app
if __name__ == '__main__':
    app.run()
