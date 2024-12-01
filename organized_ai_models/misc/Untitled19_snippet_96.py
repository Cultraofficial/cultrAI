from google.cloud import billing_v1
from datetime import datetime, timedelta
import os

# Authenticate using the Service Account Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Analyze Billing
def analyze_billing():
    try:
        print("Initializing Billing API client...")
        client = billing_v1.CloudBillingClient()

        # Specify Billing Account ID
        billing_account_name = "billingAccounts/0135D3-D70314-042927"

        # Get billing information
        print(f"Retrieving billing data for {billing_account_name}...")
        budgets = client.list_project_billing_info(name=billing_account_name)

        # Display billing information
        for budget in budgets:
            print(f"Project: {budget.project_id}, Billing Enabled: {budget.billing_enabled}")

        print("Billing data retrieval complete.")
    except Exception as e:
        print(f"Error during billing analysis: {e}")

# Run the Billing Analysis
analyze_billing()
