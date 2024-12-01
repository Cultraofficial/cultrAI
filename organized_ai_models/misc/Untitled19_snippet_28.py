from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
import time

# Path to your service account key
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"

# Authenticate using the service account
credentials = Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=[
    "https://www.googleapis.com/auth/cloud-platform"
])

# Initialize API clients
resource_manager = build('cloudresourcemanager', 'v1', credentials=credentials)
billing_service = build('cloudbilling', 'v1', credentials=credentials)
service_usage = build('serviceusage', 'v1', credentials=credentials)


def disable_all_apis(project_id):
    """Disable all enabled APIs in a project."""
    try:
        print(f"Disabling all APIs for project: {project_id}")
        services = service_usage.services().list(parent=f'projects/{project_id}').execute()
        if "services" in services:
            for service in services["services"]:
                if service["state"] == "ENABLED":
                    service_name = service["name"]
                    print(f"Disabling {service_name}...")
                    service_usage.services().disable(name=service_name).execute()
                    time.sleep(1)  # Avoid quota issues
        print(f"All APIs disabled for project: {project_id}")
    except Exception as e:
        print(f"Error disabling APIs for project {project_id}: {e}")


def delete_project(project_id):
    """Delete a Google Cloud project."""
    try:
        print(f"Deleting project: {project_id}")
        resource_manager.projects().delete(projectId=project_id).execute()
        print(f"Project {project_id} deleted successfully.")
    except Exception as e:
        print(f"Error deleting project {project_id}: {e}")


def disable_billing_account(billing_account_name):
    """Close the billing account to prevent charges."""
    try:
        print(f"Disabling billing account: {billing_account_name}")
        billing_info = billing_service.billingAccounts().get(name=billing_account_name).execute()
        if billing_info and billing_info.get("open", False):
            billing_service.billingAccounts().update(
                name=billing_account_name,
                body={"open": False}
            ).execute()
        print(f"Billing account {billing_account_name} disabled.")
    except Exception as e:
        print(f"Error disabling billing account {billing_account_name}: {e}")


# Main execution
if __name__ == "__main__":
    print("Starting full cleanup...")

    try:
        # List and delete all projects
        projects = resource_manager.projects().list().execute()
        if "projects" in projects:
            for project in projects["projects"]:
                project_id = project["projectId"]
                project_status = project["lifecycleState"]
                if project_status != "DELETE_REQUESTED":
                    disable_all_apis(project_id)
                    delete_project(project_id)
        else:
            print("No active projects found.")
    except Exception as e:
        print(f"Error listing or deleting projects: {e}")

    try:
        # List and disable billing accounts
        billing_accounts = billing_service.billingAccounts().list().execute()
        if "billingAccounts" in billing_accounts:
            for account in billing_accounts["billingAccounts"]:
                billing_account_name = account["name"]
                disable_billing_account(billing_account_name)
        else:
            print("No active billing accounts found.")
    except Exception as e:
        print(f"Error listing or disabling billing accounts: {e}")

    print("Full cleanup completed. Validating...")

    # Validation Phase
    try:
        # Re-check projects
        projects = resource_manager.projects().list().execute()
        if "projects" in projects and len(projects["projects"]) > 0:
            print("Warning: Some projects are still active.")
        else:
            print("All projects confirmed deleted.")

        # Re-check billing accounts
        billing_accounts = billing_service.billingAccounts().list().execute()
        if "billingAccounts" in billing_accounts and len(billing_accounts["billingAccounts"]) > 0:
            print("Warning: Some billing accounts are still active.")
        else:
            print("All billing accounts confirmed disabled.")

    except Exception as e:
        print(f"Error during validation: {e}")

    print("Cleanup and validation process completed.")
