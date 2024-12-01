import os
from googleapiclient.discovery import build

# Service account key path
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def check_active_projects():
    """Checks if there are any active projects remaining."""
    try:
        print("Validating active projects...")
        service = build("cloudresourcemanager", "v1")
        response = service.projects().list().execute()
        projects = response.get("projects", [])
        if not projects:
            print("All projects are fully deleted.")
        else:
            print("Active projects found:")
            for project in projects:
                print(f"- {project['name']} (ID: {project['projectId']})")
            return projects
    except Exception as e:
        print(f"Error checking projects: {e}")
        return []

def check_billing_accounts():
    """Checks if there are any active billing accounts remaining."""
    try:
        print("Validating billing accounts...")
        billing_service = build("cloudbilling", "v1")
        response = billing_service.billingAccounts().list().execute()
        accounts = response.get("billingAccounts", [])
        if not accounts:
            print("No active billing accounts found.")
        else:
            print("Active billing accounts found:")
            for account in accounts:
                print(f"- {account['name']} (Open: {account.get('open', False)})")
            return accounts
    except Exception as e:
        print(f"Error checking billing accounts: {e}")
        return []

def request_backend_cleanup():
    """Prepares data for Google Support to request backend cleanup."""
    print("\nPreparing backend cleanup request...")
    projects = check_active_projects()
    accounts = check_billing_accounts()

    if not projects and not accounts:
        print("All resources appear deleted. No further action required.")
    else:
        print("Issues detected. Please contact Google Support with the following:")
        if projects:
            print("\n--- Active Projects ---")
            for project in projects:
                print(f"Project Name: {project['name']}, Project ID: {project['projectId']}")
        if accounts:
            print("\n--- Active Billing Accounts ---")
            for account in accounts:
                print(f"Billing Account Name: {account['name']}, Open: {account.get('open', False)}")
        print("\nProvide this data to Google Support to request a backend cleanup.")

# Execute validation and support preparation
if __name__ == "__main__":
    print("Starting advanced validation and backend cleanup preparation...")
    request_backend_cleanup()
    print("Validation process completed.")
