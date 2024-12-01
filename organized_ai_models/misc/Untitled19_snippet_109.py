from googleapiclient.discovery import build

def enable_billing_export(project_id, dataset_id):
    billing = build("cloudbilling", "v1")
    billing_account_id = "0135D3-D70314-042927"  # Replace with your billing account ID

    # Enable BigQuery dataset for billing export
    try:
        response = billing.projects().updateBillingInfo(
            name=f"projects/{project_id}",
            body={
                "billingAccountName": f"billingAccounts/{billing_account_id}"
            }
        ).execute()
        print(f"Billing export enabled: {response}")
    except Exception as e:
        print(f"Failed to enable billing export: {e}")

enable_billing_export(PROJECT_ID, "billing_export")
