from google.cloud import billing_v1
from google.cloud import iam_credentials_v1
import os

# Authenticate using the Service Account Key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

# Billing Account and Service Account Information
BILLING_ACCOUNT_ID = "billingAccounts/0135D3-D70314-042927"  # Replace with your Billing Account ID
SERVICE_ACCOUNT_EMAIL = "cultra-115@gen-lang-client-0492208227.iam.gserviceaccount.com"

def add_billing_viewer_role():
    try:
        print("Initializing Billing Client...")
        billing_client = billing_v1.CloudBillingClient()

        # Get current IAM policy for the billing account
        resource = BILLING_ACCOUNT_ID
        policy = billing_client.get_iam_policy(request={"resource": resource})

        print("Checking existing roles...")
        role_exists = False
        for binding in policy.bindings:
            if binding.role == "roles/billing.viewer":
                if f"serviceAccount:{SERVICE_ACCOUNT_EMAIL}" in binding.members:
                    role_exists = True
                    print(f"Service account {SERVICE_ACCOUNT_EMAIL} already has 'Billing Account Viewer' role.")
                    break

        # If the role doesn't exist, add it
        if not role_exists:
            print(f"Adding 'Billing Account Viewer' role to {SERVICE_ACCOUNT_EMAIL}...")
            new_binding = {
                "role": "roles/billing.viewer",
                "members": [f"serviceAccount:{SERVICE_ACCOUNT_EMAIL}"],
            }
            policy.bindings.append(new_binding)

            # Update the IAM policy
            updated_policy = billing_client.set_iam_policy(
                request={"resource": resource, "policy": policy}
            )
            print(f"'Billing Account Viewer' role successfully assigned to {SERVICE_ACCOUNT_EMAIL}.")
        else:
            print("No changes made. The role already exists.")

    except Exception as e:
        print(f"Error during role assignment: {e}")

# Run the Function
add_billing_viewer_role()
