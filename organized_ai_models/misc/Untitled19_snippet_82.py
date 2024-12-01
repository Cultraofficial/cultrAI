from google.cloud import billing_v1
from google.cloud import aiplatform
import os
from datetime import datetime, timedelta

# Step 1: Authenticate using your service account key
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Update path if needed
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
print("Authenticated with the service account.")

# Step 2: Test Billing API Permissions
def test_billing_api():
    try:
        client = billing_v1.CloudBillingClient()
        print("Billing API successfully initialized. Permissions are working!")
        return True
    except Exception as e:
        print(f"Permission error: {e}")
        print("Please ensure the service account has the Billing Account Viewer role.")
        return False

# Step 3: Analyze Billing Costs (if permissions are working)
def analyze_billing_costs():
    client = billing_v1.CloudBillingClient()
    billing_account_name = "billingAccounts/0135D3-D70314-042927"  # Replace with your billing account ID

    # Define time range (last 7 days)
    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)

    print(f"\nAnalyzing costs from {start_time} to {end_time}...")
    try:
        # List billing projects associated with the account
        request = billing_v1.ListProjectBillingInfoRequest(name=billing_account_name)
        results = client.list_project_billing_info(request=request)

        for result in results:
            print(f"Project: {result.project_id}, Billing Enabled: {result.billing_enabled}")

        print("\nBilling analysis completed!")
    except Exception as e:
        print(f"Error occurred while retrieving billing data: {e}")

# Step 4: Run everything
if test_billing_api():
    analyze_billing_costs()
else:
    print("Check permissions and try again.")
