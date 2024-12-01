from google.cloud import billing_v1
from google.auth import exceptions
import os

# Automatically configure credentials
SERVICE_ACCOUNT_JSON = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_JSON


def list_billing_accounts():
    """List all billing accounts under the current credentials."""
    try:
        billing_client = billing_v1.CloudBillingClient()
        print("Fetching all billing accounts...")
        billing_accounts = billing_client.list_billing_accounts()
        account_list = []
        for account in billing_accounts:
            print(f"Billing Account Found: {account.name} (Open: {account.open})")
            account_list.append(account)
        return account_list
    except exceptions.GoogleAuthError as e:
        print(f"Authentication error: {e}")
        return []
    except Exception as e:
        print(f"Error fetching billing accounts: {e}")
        return []


def disable_billing_account(billing_account_name):
    """Disable the billing account to prevent future charges."""
    try:
        billing_client = billing_v1.CloudBillingClient()
        print(f"Disabling billing account: {billing_account_name}...")
        billing_client.update_billing_account(
            name=billing_account_name,
            account={"open": False},
        )
        print(f"Billing account {billing_account_name} has been disabled.")
    except Exception as e:
        print(f"Error disabling billing account {billing_account_name}: {e}")


def cleanup_billing():
    """Main function to cleanup all billing accounts."""
    billing_accounts = list_billing_accounts()

    if not billing_accounts:
        print("No billing accounts found or accessible.")
        return

    for account in billing_accounts:
        if account.open:
            print(f"Attempting to disable billing for account: {account.name}...")
            disable_billing_account(account.name)

    print("Billing cleanup completed. No further charges will occur.")


# Main Execution
if __name__ == "__main__":
    print("Starting automated billing cleanup...")
    cleanup_billing()
    print("All billing accounts processed.")
