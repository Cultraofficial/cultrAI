from google.cloud import billing_v1
from datetime import datetime, timedelta

def analyze_vertex_ai_costs():
    # Initialize the Billing API client
    client = billing_v1.CloudBillingClient()

    # Replace with your billing account ID
    billing_account_name = "billingAccounts/0135D3-D70314-042927"

    # Define time period (last 7 days)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)

    print(f"Analyzing costs from {start_time} to {end_time}...")
    results = client.list_project_billing_info(name=billing_account_name)

    for result in results:
        print(f"Project: {result.project_id}, Billing Enabled: {result.billing_enabled}")

analyze_vertex_ai_costs()
