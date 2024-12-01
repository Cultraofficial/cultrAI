from google.cloud import billing_v1
import os
from datetime import datetime, timedelta

# Authenticate using your Service Account Key
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Update path if necessary
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
print("Authenticated with the service account.")

# Billing Account ID
BILLING_ACCOUNT_ID = "billingAccounts/0135D3-D70314-042927"  # Replace with your Billing Account ID

# Step 1: Test the Billing API
def test_billing_api():
    try:
        client = billing_v1.CloudBillingClient()
        print("Billing API successfully initialized.")
        return True
    except Exception as e:
        print(f"Error initializing Billing API: {e}")
        return False

# Step 2: Analyze Billing Data
def analyze_billing_data():
    try:
        client = billing_v1.CloudBillingClient()
        end_time = datetime.utcnow()
        start_time = end_time - timedelta(days=7)
        print(f"\nAnalyzing costs from {start_time} to {end_time}...")

        request = billing_v1.ListProjectBillingInfoRequest(name=BILLING_ACCOUNT_ID)
        results = client.list_project_billing_info(request=request)

        print("\nBilling Information:")
        for result in results:
            print(f"Project ID: {result.project_id}, Billing Enabled: {result.billing_enabled}")
        print("\nBilling analysis complete!")
    except Exception as e:
        if "403" in str(e):
            print("\nPermission Error: The service account does not have the required permissions.")
            print("Ensure the service account has the 'Billing Account Viewer' role at the billing account level.")
        else:
            print(f"Error occurred during billing analysis: {e}")

# Run the Workflow
if test_billing_api():
    analyze_billing_data()
else:
    print("Ensure the Cloud Billing API is enabled in your Google Cloud Console.")
