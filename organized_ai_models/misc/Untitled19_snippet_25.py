import os
from googleapiclient.discovery import build

# Service account key path
SERVICE_ACCOUNT_FILE = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_FILE

def validate_services():
    """Checks and disables any lingering API services."""
    try:
        print("Validating and disabling all API services...")
        service_usage = build("serviceusage", "v1")
        request = service_usage.services().list(parent="projects/-")
        response = request.execute()
        services = response.get("services", [])
        for service in services:
            if service.get("state") == "ENABLED":
                print(f"Disabling API: {service['name']}...")
                service_usage.services().disable(name=service["name"]).execute()
                print(f"Disabled API: {service['name']}")
        if not services:
            print("No active API services found.")
    except Exception as e:
        print(f"Error disabling API services: {e}")

def validate_quotas():
    """Checks if any quotas are still active."""
    try:
        print("Validating quotas...")
        quota_service = build("serviceconsumermanagement", "v1")
        request = quota_service.services().list(parent="projects/-")
        response = request.execute()
        quotas = response.get("quotas", [])
        if not quotas:
            print("All quotas are reset to zero.")
        else:
            print("Active quotas detected:")
            for quota in quotas:
                print(f"- {quota['metric']}: {quota['usage']}")
    except Exception as e:
        print(f"Error validating quotas: {e}")

def generate_support_report():
    """Generates a report for Google Support."""
    print("\nGenerating detailed support report...")
    print("If any lingering resources or quotas are found, provide this log to Google Support.")
    print("\n--- API Service Validation ---")
    validate_services()
    print("\n--- Quota Validation ---")
    validate_quotas()
    print("\n--- Report Generation Complete ---")
    print("Proceed to submit this information to Google Support if necessary.")

# Execute advanced validation
if __name__ == "__main__":
    print("Starting advanced validation and final cleanup...")
    generate_support_report()
    print("Advanced validation process completed.")
