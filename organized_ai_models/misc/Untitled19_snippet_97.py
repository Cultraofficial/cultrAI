from google.cloud import aiplatform
from datetime import datetime, timedelta
import os

# Authenticate using the Service Account Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Initialize AI Platform
aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

def analyze_vertex_ai_usage():
    print("Checking Vertex AI Endpoints...")
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")

    print("\nChecking Vertex AI Training Jobs...")
    jobs = aiplatform.CustomJob.list()
    for job in jobs:
        print(f"Training Job: {job.display_name}, State: {job.state}, Resource Name: {job.resource_name}")

    print("\nChecking Vertex AI Pipelines...")
    pipelines = aiplatform.PipelineJob.list()
    if not pipelines:
        print("No active pipelines found.")
    for pipeline in pipelines:
        print(f"Pipeline: {pipeline.display_name}, State: {pipeline.state}")

    print("\nChecking Vertex AI Batch Predictions...")
    batch_predictions = aiplatform.BatchPredictionJob.list()
    for batch in batch_predictions:
        print(f"Batch Prediction: {batch.display_name}, State: {batch.state}")

analyze_vertex_ai_usage()
