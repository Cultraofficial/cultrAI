from flask import Flask, request, jsonify
from google.cloud import aiplatform

app = Flask(__name__)
project = "gen-lang-client-0492208227"
location = "us-central1"

aiplatform.init(project=project, location=location)

# Example route for a deployed model
@app.route("/predict/<model_id>", methods=["POST"])
def predict(model_id):
    content = request.json
    endpoint = aiplatform.Endpoint(model_id)
    prediction = endpoint.predict([content['input_data']])
    return jsonify(prediction)
