# Install necessary libraries
!pip install google-cloud-aiplatform google-cloud-storage --quiet

# Import required libraries
from google.cloud import aiplatform, storage
import time

# Project details (automatically applied from previous context)
PROJECT_ID = "gen-lang-client-0492208227"  # Your Google Cloud Project ID
REGION = "us-central1"  # Default region for Vertex AI services
BUCKET_NAME = "cultra_official"  # Confirmed storage bucket

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# Function to list and stop unnecessary endpoints
def stop_unused_endpoints():
    print("Checking active endpoints...")
    endpoints = aiplatform.Endpoint.list()
    if not endpoints:
        print("No active endpoints found.")
        return

    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")
        if input(f"Pause {endpoint.display_name}? (yes/no): ").lower() == "yes":
            endpoint.undeploy_all()
            print(f"Paused endpoint: {endpoint.display_name}")
        else:
            print(f"Skipping: {endpoint.display_name}")

# Function to analyze current usage and find costly resources
def analyze_costs():
    print("Analyzing costs...")
    print("You can review your billing data directly at https://console.cloud.google.com/billing.")
    print("Focus on Vertex AI and check which models or endpoints are consuming resources.")
    # (Optionally connect to BigQuery for real-time cost analysis if billing export is set up.)

# Function to optimize deployed resources
def optimize_resources():
    print("Optimizing active resources...")
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Optimizing endpoint: {endpoint.display_name}")
        # Set replicas to 1 and use cost-efficient machine types
        endpoint.update(
            min_replica_count=1,
            max_replica_count=1,
        )
        print(f"Optimized: {endpoint.display_name} to 1 replica.")

# Function to shift non-critical tasks to Google Colab
def shift_to_colab():
    print("Moving non-critical tasks to Colab...")
    print("Use Google Colab for development and lightweight tasks to avoid cloud costs.")
    print("Example: Loading and testing AI models locally.")

    # Example: Load a model locally using transformers
    try:
        from transformers import AutoModel, AutoTokenizer
        model_name = "EleutherAI/gpt-neo-125M"
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)
        print(f"Model {model_name} loaded locally for testing.")
    except Exception as e:
        print(f"Error loading model locally: {e}")

# Function to set up monitoring and alerts
def setup_alerts():
    print("Setting up cost alerts...")
    # Cost alerts need to be configured directly in the Google Cloud Billing console
    print("Go to https://console.cloud.google.com/billing/alerts to configure budget alerts.")
    print("Set alerts to trigger when spending exceeds $500 to catch issues early.")

# Main workflow
def main():
    print("Starting Vertex AI troubleshooting...")

    # Step 1: Stop unused endpoints to cut costs
    stop_unused_endpoints()

    # Step 2: Analyze costs and find high-cost resources
    analyze_costs()

    # Step 3: Optimize active resources to minimize charges
    optimize_resources()

    # Step 4: Shift non-critical tasks to Colab
    shift_to_colab()

    # Step 5: Set up future alerts for cost management
    setup_alerts()

    print("All steps completed. Review active resources and confirm cost reductions.")

# Run the workflow
main()
