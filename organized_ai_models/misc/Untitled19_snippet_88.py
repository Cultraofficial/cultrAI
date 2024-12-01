from google.cloud import billing_v1
from datetime import datetime, timedelta
import os

# Authenticate using the Service Account Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Billing Account and Project Information
BILLING_ACCOUNT_ID = "billingAccounts/0135D3-D70314-042927"  # Replace with your Billing Account ID
PROJECT_ID = "gen-lang-client-0492208227"  # Your Google Cloud project ID

def analyze_vertex_ai_billing():
    try:
        # Initialize the Billing Client
        billing_client = billing_v1.CloudBillingClient()
        print("Billing API successfully initialized.")

        # Define the time range for analysis (last 7 days)
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=7)
        print(f"Analyzing billing data from {start_time} to {end_time}...")

        # Fetch billing information
        request = billing_v1.ListProjectBillingInfoRequest(name=BILLING_ACCOUNT_ID)
        project_billing_info = billing_client.list_project_billing_info(request=request)

        print("\nBilling Information:")
        for billing_info in project_billing_info:
            print(f"Project ID: {billing_info.project_id}, Billing Enabled: {billing_info.billing_enabled}")

        # Analyze Vertex AI charges
        print("\nAnalyzing Vertex AI charges specifically...")
        vertex_ai_charges = {}  # Dictionary to store Vertex AI-related costs
        for billing_item in project_billing_info:
            if "Vertex AI" in billing_item.project_id:  # Example filter
                vertex_ai_charges[billing_item.project_id] = billing_item.billing_enabled

        # Display findings
        if vertex_ai_charges:
            print("\nVertex AI Billing Details:")
            for project, billing in vertex_ai_charges.items():
                print(f"Project: {project}, Billing Enabled: {billing}")
        else:
            print("No Vertex AI charges found.")

        print("\nBilling analysis completed. If charges seem abnormal, consider disputing.")
    except Exception as e:
        print(f"Error during billing analysis: {e}")

# Run the Analysis
analyze_vertex_ai_billing()
