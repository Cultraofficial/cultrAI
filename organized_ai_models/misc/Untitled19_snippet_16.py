import os
from googleapiclient.discovery import build
from google.cloud import storage

# Set up service account key
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/service_account_key.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def list_projects():
    """Lists all projects in the account."""
    print("Listing all projects...")
    try:
        service = build("cloudresourcemanager", "v1")
        request = service.projects().list()
        response = request.execute()
        projects = response.get("projects", [])
        if not projects:
            print("No projects found.")
        else:
            for project in projects:
                print(f"Project: {project['name']} (ID: {project['projectId']})")
        return projects
    except Exception as e:
        print(f"Error listing projects: {e}")
        return []

def delete_project(project_id):
    """Deletes a project."""
    try:
        print(f"Deleting project: {project_id}...")
        service = build("cloudresourcemanager", "v1")
        request = service.projects().delete(projectId=project_id)
        request.execute()
        print(f"Project {project_id} deleted successfully!")
    except Exception as e:
        print(f"Error deleting project {project_id}: {e}")

def disable_billing(project_id):
    """Disables billing for a project."""
    try:
        print(f"Disabling billing for project: {project_id}...")
        billing_service = build("cloudbilling", "v1")
        billing_info = f"projects/{project_id}/billingInfo"
        billing_service.projects().updateBillingInfo(
            name=billing_info,
            body={"billingAccountName": ""}
        ).execute()
        print(f"Billing disabled for project {project_id}.")
    except Exception as e:
        print(f"Error disabling billing for project {project_id}: {e}")

def disable_all_apis(project_id):
    """Disables all APIs for a project."""
    try:
        print(f"Disabling all APIs for project: {project_id}...")
        service_usage = build("serviceusage", "v1")
        request = service_usage.services().list(parent=f"projects/{project_id}")
        response = request.execute()
        for service in response.get("services", []):
            if service["state"] == "ENABLED":
                service_name = service["name"]
                print(f"Disabling API: {service_name}...")
                service_usage.services().disable(
                    name=service_name
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

def list_and_delete_billing_accounts():
    """Lists and deletes all billing accounts."""
    try:
        print("Listing billing accounts...")
        billing_service = build("cloudbilling", "v1")
        accounts = billing_service.billingAccounts().list().execute()
        for account in accounts.get("billingAccounts", []):
            if account.get("open", False):
                print(f"Closing billing account: {account['name']}...")
                billing_service.billingAccounts().close(name=account["name"]).execute()
                print(f"Billing account {account['name']} closed successfully.")
    except Exception as e:
        print(f"Error listing or deleting billing accounts: {e}")

def cleanup():
    """Performs a complete cleanup of all Google Cloud resources."""
    print("Starting complete cleanup...")
    projects = list_projects()

    for project in projects:
        project_id = project["projectId"]
        # Disable billing
        disable_billing(project_id)
        # Disable all APIs
        disable_all_apis(project_id)
        # Delete storage buckets
        delete_storage_buckets(project_id)
        # Delete the project
        delete_project(project_id)

    # Delete all billing accounts
    list_and_delete_billing_accounts()
    print("Complete cleanup finished. All projects, APIs, and billing accounts have been processed.")

# Execute the cleanup
if __name__ == "__main__":
    cleanup()
