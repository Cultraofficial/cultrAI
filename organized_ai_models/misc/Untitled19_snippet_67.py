from google.cloud import aiplatform

# Authenticate with your service account
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

def check_vertex_ai_resources():
    print("Checking Vertex AI Endpoints...")
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")

    print("\nChecking Vertex AI Training Jobs...")
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        print(f"Training Job: {job.display_name}, State: {job.state}, Resource Name: {job.resource_name}")

    print("\nChecking Vertex AI Batch Predictions...")
    batch_predictions = aiplatform.BatchPredictionJob.list()
    for prediction in batch_predictions:
        print(f"Batch Prediction: {prediction.display_name}, State: {prediction.state}, Resource Name: {prediction.resource_name}")

check_vertex_ai_resources()
