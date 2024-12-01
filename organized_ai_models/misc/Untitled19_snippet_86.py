from google.cloud import billing_v1, iam_v1
from google.iam.v1 import iam_policy_pb2
import os

# Service Account and Billing Info
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Update path if necessary
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
BILLING_ACCOUNT_ID = "billingAccounts/0135D3-D70314-042927"  # Replace with your Billing Account ID

print("Authenticated with the service account.")

# Step 1: Test Billing API Access
def test_billing_api():
    try:
        client = billing_v1.CloudBillingClient()
        print("Billing API successfully initialized.")
        return True
    except Exception as e:
        print(f"Error initializing Billing API: {e}")
        return False

# Step 2: Check and Attempt to Fix Permissions
def check_and_fix_permissions():
    try:
        print("Checking permissions...")
        iam_client = iam_v1.PolicyServiceClient()
        request = iam_policy_pb2.GetIamPolicyRequest(resource=BILLING_ACCOUNT_ID)
        policy = iam_client.get_iam_policy(request=request)

        # Check if the service account already has the role
        service_account_email = SERVICE_ACCOUNT_KEY.split("/")[-1].replace(".json", "")
        role_exists = any(
            binding.role == "roles/billing.viewer" and f"serviceAccount:{service_account_email}" in binding.members
            for binding in policy.bindings
        )

        if role_exists:
            print(f"Service account already has 'Billing Account Viewer' role.")
            return True
        else:
            print(f"Adding 'Billing Account Viewer' role to service account...")
            # Add the role to the service account
            policy.bindings.append(
                {
                    "role": "roles/billing.viewer",
                    "members": [f"serviceAccount:{service_account_email}"],
                }
            )
            request = iam_policy_pb2.SetIamPolicyRequest(resource=BILLING_ACCOUNT_ID, policy=policy)
            iam_client.set_iam_policy(request=request)
            print("Role successfully added!")
            return True
    except Exception as e:
        print(f"Permission Fix Error: {e}")
        return False

# Step 3: Analyze Billing Data
def analyze_billing_data():
    try:
        client = billing_v1.CloudBillingClient()
        print("\nAnalyzing costs...")
        results = client.list_project_billing_info(name=BILLING_ACCOUNT_ID)

        for result in results:
            print(f"Project ID: {result.project_id}, Billing Enabled: {result.billing_enabled}")
        print("\nBilling analysis complete!")
    except Exception as e:
        print(f"Error occurred during billing analysis: {e}")

# Run Workflow
def run_workflow():
    if not test_billing_api():
        print("Ensure the Cloud Billing API is enabled and try again.")
        return

    if not check_and_fix_permissions():
        print("\nPermissions could not be fixed automatically.")
        print("Ensure the service account has 'Billing Account Viewer' role and try again.")
        return

    analyze_billing_data()

run_workflow()
