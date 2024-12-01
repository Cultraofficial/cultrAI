from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    # Add any additional processing or database code here
    return jsonify({"status": "success", "data": data})

if __name__ == '__main__':
    app.run()
