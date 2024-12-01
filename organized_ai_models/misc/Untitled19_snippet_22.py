import os
from googleapiclient.discovery import build

# Service account key path
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def validate_deleted_projects():
    """Attempts to list projects and validates their deletion."""
    try:
        print("Checking projects for deletion...")
        service = build("cloudresourcemanager", "v1")
        response = service.projects().list().execute()
        projects = response.get("projects", [])
        if not projects:
            print("All projects are fully deleted.")
        else:
            print("Some projects still exist. Here's the list:")
            for project in projects:
                print(f"- {project['name']} (ID: {project['projectId']})")
    except Exception as e:
        print(f"Error validating projects: {e}")

def validate_billing_accounts():
    """Attempts to list billing accounts and confirms their status."""
    try:
        print("Checking billing accounts...")
        billing_service = build("cloudbilling", "v1")
        response = billing_service.billingAccounts().list().execute()
        accounts = response.get("billingAccounts", [])
        if not accounts:
            print("All billing accounts are fully deleted or inaccessible.")
        else:
            print("Some billing accounts still exist. Here's the list:")
            for account in accounts:
                print(f"- {account['name']} (Open: {account.get('open', False)})")
    except Exception as e:
        print(f"Error validating billing accounts: {e}")

def validate_and_report():
    """Runs validation and prepares a detailed support report."""
    print("Starting validation and report generation...")
    print("\n--- Validating Deleted Projects ---")
    validate_deleted_projects()
    print("\n--- Validating Billing Accounts ---")
    validate_billing_accounts()
    print("\n--- Validation Complete ---")
    print(
        "If issues persist, provide this report to Google Support. "
        "No further actions are required if everything is confirmed deleted."
    )

# Execute validation
if __name__ == "__main__":
    validate_and_report()
