import os
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from google.cloud import resource_manager_v3, billing_v1
from google.cloud import storage
from googleapiclient.discovery import build

# Constants
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/service_account_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def list_all_projects():
    """Lists all projects in the account."""
    print("Listing all projects...")
    try:
        client = resource_manager_v3.ProjectsClient()
        projects = list(client.list_projects())
        if not projects:
            print("No projects found.")
        else:
            for project in projects:
                print(f"Project: {project.display_name} ({project.name})")
        return projects
    except Exception as e:
        print(f"Error listing projects: {e}")
        return []

def delete_project(project_id):
    """Deletes a project."""
    try:
        print(f"Deleting project: {project_id}...")
        client = resource_manager_v3.ProjectsClient()
        client.delete_project(name=f"projects/{project_id}")
        print(f"Project {project_id} deleted successfully!")
    except Exception as e:
        print(f"Error deleting project {project_id}: {e}")

def disable_billing(project_id):
    """Disables billing for a project."""
    try:
        print(f"Disabling billing for project: {project_id}...")
        billing_client = billing_v1.CloudBillingClient()
        billing_name = f"projects/{project_id}/billingInfo"
        billing_client.update_project_billing_info(
            name=billing_name,
            project_billing_info={"billing_account_name": ""}
        )
        print(f"Billing disabled for project {project_id}.")
    except Exception as e:
        print(f"Error disabling billing for project {project_id}: {e}")

def delete_billing_account(billing_account_name):
    """Deletes a billing account."""
    try:
        print(f"Deleting billing account: {billing_account_name}...")
        billing_client = billing_v1.CloudBillingClient()
        billing_client.close_billing_account(name=billing_account_name)
        print(f"Billing account {billing_account_name} closed successfully.")
    except Exception as e:
        print(f"Error deleting billing account {billing_account_name}: {e}")

def disable_all_apis(project_id):
    """Disables all enabled APIs for a project."""
    try:
        print(f"Disabling all APIs for project: {project_id}...")
        service_usage = build("serviceusage", "v1")
        services = service_usage.services().list(parent=f"projects/{project_id}").execute()
        for service in services.get("services", []):
            if service["state"] == "ENABLED":
                service_name = service["name"].split("/")[-1]
                print(f"Disabling API: {service_name}...")
                service_usage.services().disable(
                    name=f"projects/{project_id}/services/{service_name}"
                ).execute()
                print(f"Disabled API: {service_name}.")
    except Exception as e:
        print(f"Error disabling APIs for project {project_id}: {e}")

def delete_storage_buckets(project_id):
    """Deletes all storage buckets in a project."""
    try:
        print(f"Deleting all storage buckets for project: {project_id}...")
        storage_client = storage.Client(project=project_id)
        buckets = list(storage_client.list_buckets())
        for bucket in buckets:
            print(f"Deleting bucket: {bucket.name}...")
            bucket.delete(force=True)
            print(f"Deleted bucket: {bucket.name}.")
    except Exception as e:
        print(f"Error deleting storage buckets for project {project_id}: {e}")

def cleanup():
    """Performs a complete cleanup of the Google Cloud account."""
    print("Starting complete cleanup...")
    projects = list_all_projects()

    for project in projects:
        project_id = project.project_id
        # Disable billing
        disable_billing(project_id)
        # Disable all APIs
        disable_all_apis(project_id)
        # Delete storage buckets
        delete_storage_buckets(project_id)
        # Delete the project
        delete_project(project_id)

    print("Checking for billing accounts...")
    try:
        billing_client = billing_v1.CloudBillingClient()
        billing_accounts = billing_client.list_billing_accounts()
        for account in billing_accounts:
            if account.open:
                delete_billing_account(account.name)
    except Exception as e:
        print(f"Error listing or deleting billing accounts: {e}")

    print("Complete cleanup finished. All projects, APIs, and billing accounts have been processed.")

# Execute the cleanup
if __name__ == "__main__":
    cleanup()
