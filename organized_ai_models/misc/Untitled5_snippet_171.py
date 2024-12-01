from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    add_document("Users", data, document_id=data.get("user_id"))
    return jsonify({"status": "User added successfully"})

@app.route('/get_user/<user_id>', methods=['GET'])
def get_user(user_id):
    user_data = get_document("Users", user_id)
    return jsonify(user_data if user_data else {"error": "User not found"})

@app.route('/update_user/<user_id>', methods=['PATCH'])
def update_user(user_id):
    data = request.json
    update_document("Users", user_id, data)
    return jsonify({"status": "User updated successfully"})

@app.route('/delete_user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    delete_document("Users", user_id)
    return jsonify({"status": "User deleted successfully"})

# Run Flask application
if __name__ == "__main__":
    app.run(port=5000)
