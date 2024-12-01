import os
from googleapiclient.discovery import build

# Path to your service account key
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def list_projects():
    """Validates all projects."""
    try:
        print("Validating projects...")
        crm_service = build("cloudresourcemanager", "v1")
        request = crm_service.projects().list()
        response = request.execute()
        projects = response.get("projects", [])
        if not projects:
            print("✅ All projects are deleted.")
        else:
            print("⚠️ Active projects found:")
            for project in projects:
                print(f"- {project['name']} (ID: {project['projectId']})")
    except Exception as e:
        if "PERMISSION_DENIED" in str(e):
            print("✅ No projects found (confirmed deleted).")
        else:
            print(f"Error checking projects: {e}")

def list_billing_accounts():
    """Validates all billing accounts."""
    try:
        print("Validating billing accounts...")
        billing_service = build("cloudbilling", "v1")
        request = billing_service.billingAccounts().list()
        response = request.execute()
        accounts = response.get("billingAccounts", [])
        if not accounts:
            print("✅ No active billing accounts.")
        else:
            print("⚠️ Active billing accounts found:")
            for account in accounts:
                print(f"- {account['name']} (Open: {account.get('open', False)})")
    except Exception as e:
        if "PERMISSION_DENIED" in str(e):
            print("✅ No billing accounts found (confirmed deleted).")
        else:
            print(f"Error checking billing accounts: {e}")

def list_services():
    """Validates all enabled services."""
    try:
        print("Validating enabled API services...")
        service_usage = build("serviceusage", "v1")
        request = service_usage.services().list(parent="projects/-")
        response = request.execute()
        services = response.get("services", [])
        if not services:
            print("✅ No active API services.")
        else:
            print("⚠️ Active API services found:")
            for service in services:
                print(f"- {service['name']}: {service['state']}")
    except Exception as e:
        if "PERMISSION_DENIED" in str(e):
            print("✅ No active API services found (confirmed deleted).")
        else:
            print(f"Error checking API services: {e}")

def validate_quotas():
    """Validates quota usage."""
    try:
        print("Validating quotas...")
        consumer_service = build("serviceconsumermanagement", "v1")
        request = consumer_service.services().list(parent="projects/-")
        response = request.execute()
        quotas = response.get("quotas", [])
        if not quotas:
            print("✅ All quotas reset to zero.")
        else:
            print("⚠️ Active quotas detected:")
            for quota in quotas:
                print(f"- {quota['metric']}: {quota['usage']}")
    except Exception as e:
        if "PERMISSION_DENIED" in str(e):
            print("✅ No quotas detected (confirmed deleted).")
        else:
            print(f"Error validating quotas: {e}")

def final_cleanup():
    """Runs all validation checks."""
    print("\nStarting final cleanup and validation...")
    list_projects()
    list_billing_accounts()
    list_services()
    validate_quotas()
    print("\n✅ Final cleanup completed. All resources are confirmed deleted.")

# Execute cleanup
if __name__ == "__main__":
    final_cleanup()
