from google.cloud import resource_manager
from google.cloud import billing_v1
import os

# Authenticate using the Service Account Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Billing Account and Service Account Information
BILLING_ACCOUNT_ID = "billingAccounts/0135D3-D70314-042927"  # Replace with your Billing Account ID
SERVICE_ACCOUNT_EMAIL = "cultra-115@gen-lang-client-0492208227.iam.gserviceaccount.com"

def check_and_add_billing_permissions():
    try:
        print("Checking IAM policy for billing account...")

        # Initialize the Billing Client
        billing_client = billing_v1.CloudBillingClient()
        resource = f"{BILLING_ACCOUNT_ID}"

        # Get current IAM policy
        policy = billing_client.get_iam_policy(resource=resource)

        # Check if service account has Billing Account Viewer role
        role_found = False
        for binding in policy.bindings:
            if binding.role == "roles/billing.viewer":
                if SERVICE_ACCOUNT_EMAIL in binding.members:
                    role_found = True
                    print(f"Service account {SERVICE_ACCOUNT_EMAIL} already has 'Billing Account Viewer' role.")
                    break

        # Add Billing Account Viewer role if not found
        if not role_found:
            print(f"Adding 'Billing Account Viewer' role to {SERVICE_ACCOUNT_EMAIL}...")
            policy.bindings.append({
                "role": "roles/billing.viewer",
                "members": [f"serviceAccount:{SERVICE_ACCOUNT_EMAIL}"]
            })
            billing_client.set_iam_policy(resource=resource, policy=policy)
            print(f"'Billing Account Viewer' role successfully assigned to {SERVICE_ACCOUNT_EMAIL}.")

    except Exception as e:
        print(f"Error during IAM policy modification: {e}")

# Run the Function
check_and_add_billing_permissions()
