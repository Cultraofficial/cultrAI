from google.cloud import billing_v1
from google.cloud import iam_v1
import os
from datetime import datetime, timedelta

# Step 1: Authenticate using the Service Account Key
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Update path if necessary
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
print("Authenticated with the service account.")

# Step 2: Check Billing API Permissions
def check_billing_permissions():
    try:
        client = billing_v1.CloudBillingClient()
        print("Billing API successfully initialized. Checking permissions...")
        return True
    except Exception as e:
        print(f"Error initializing Billing API: {e}")
        return False

# Step 3: Test IAM Permissions
def test_iam_permissions(billing_account_name):
    print("\nTesting IAM permissions...")
    try:
        # Initialize IAM Policy Client
        iam_client = iam_v1.PolicyAnalyzerClient()

        # Set up permissions to check
        permissions = ["billing.accounts.get", "billing.accounts.list"]

        # Request to test IAM permissions
        request = iam_v1.TestIamPermissionsRequest(
            resource=billing_account_name,
            permissions=permissions
        )
        response = iam_client.test_iam_permissions(request=request)

        # Check if all permissions are granted
        missing_permissions = [perm for perm in permissions if perm not in response.permissions]
        if not missing_permissions:
            print("All required permissions are present.")
            return True
        else:
            print(f"Missing permissions: {missing_permissions}")
            return False
    except Exception as e:
        print(f"Error testing IAM permissions: {e}")
        return False

# Step 4: Analyze Billing Costs
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

# Step 5: Attempt to Fix Permissions (If Missing)
def attempt_to_fix_permissions(billing_account_name):
    print("\nAttempting to fix permissions...")
    try:
        client = iam_v1.PolicyServiceClient()

        # Add Billing Account Viewer Role
        policy = client.get_iam_policy(resource=billing_account_name)
        policy.bindings.append(
            {
                "role": "roles/billing.viewer",
                "members": [f"serviceAccount:{SERVICE_ACCOUNT_KEY}"]
            }
        )
        client.set_iam_policy(resource=billing_account_name, policy=policy)
        print("Billing Account Viewer role assigned to the service account.")
        return True
    except Exception as e:
        print(f"Error attempting to fix permissions: {e}")
        return False

# Run the Full Workflow
def run_workflow():
    billing_account_name = "billingAccounts/0135D3-D70314-042927"

    if not check_billing_permissions():
        print("Billing API is not working. Ensure the Cloud Billing API is enabled.")
        return

    if not test_iam_permissions(billing_account_name):
        print("Missing permissions detected.")
        if attempt_to_fix_permissions(billing_account_name):
            print("Permissions fixed. Retrying billing analysis...")
            analyze_billing_costs()
        else:
            print("Could not fix permissions automatically. Contact admin to assign Billing Account Viewer role.")
    else:
        print("Permissions are correct. Proceeding to billing analysis...")
        analyze_billing_costs()

run_workflow()
