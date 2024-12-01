# Flask setup in Colab (for development, this should be deployed on a server)

!pip install flask flask_cors google-cloud-firestore

from flask import Flask, request, jsonify
from google.cloud import firestore
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow cross-origin requests for front-end integration

# Initialize Firestore client
db = firestore.Client(project="gen-lang-client-0492208227")

# Sample endpoint for user interaction logging
@app.route('/log_interaction', methods=['POST'])
def log_interaction():
    data = request.json
    interaction_type = data.get("interaction_type")
    interaction_data = data.get("data")
    doc_ref = db.collection('viewer_interactions').document()
    doc_ref.set({
        'interaction_type': interaction_type,
        'data': interaction_data,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    return jsonify({"status": "Interaction logged"}), 200

# Run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
