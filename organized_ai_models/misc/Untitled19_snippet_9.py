from google.cloud import billing_v1
from google.cloud.resourcemanager_v3 import ProjectsClient
import os

# Automatically configure credentials
SERVICE_ACCOUNT_JSON = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_JSON

def list_billing_projects():
    """List all projects linked to a billing account."""
    try:
        billing_client = billing_v1.CloudBillingClient()
        projects_client = ProjectsClient()

        print("Listing all active projects with billing accounts...")
        active_projects = [
            project for project in projects_client.list_projects() if project.state.name == "ACTIVE"
        ]
        for project in active_projects:
            project_billing_info = billing_client.get_project_billing_info(name=f"projects/{project.project_id}")
            if project_billing_info.billing_account_name:
                print(f"Project {project.project_id} is linked to billing account: {project_billing_info.billing_account_name}")
            else:
                print(f"Project {project.project_id} has no billing account linked.")
        return active_projects
    except Exception as e:
        print(f"Error listing projects or billing information: {e}")
        return []

def disable_billing_for_all():
    """Disable billing for all active projects."""
    try:
        billing_client = billing_v1.CloudBillingClient()
        projects = list_billing_projects()

        for project in projects:
            project_id = project.project_id
            print(f"Disabling billing for project {project_id}...")
            try:
                billing_client.update_project_billing_info(
                    name=f"projects/{project_id}/billingInfo",
                    project_billing_info={"billing_account_name": ""},
                )
                print(f"Billing disabled for project {project_id}.")
            except Exception as inner_e:
                print(f"Error disabling billing for project {project_id}: {inner_e}")
    except Exception as e:
        print(f"Error disabling billing for projects: {e}")

# Main Execution
if __name__ == "__main__":
    print("Disabling billing for all active projects...")
    disable_billing_for_all()
    print("Billing cleanup completed.")
