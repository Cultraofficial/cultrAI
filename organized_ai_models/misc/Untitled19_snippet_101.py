from google.cloud import billing_v1
import datetime

def analyze_vertex_ai_costs():
    print("Initializing Billing Client...")
    billing_client = billing_v1.CloudBillingClient()

    # Set your billing account ID
    billing_account_name = "billingAccounts/0135D3-D70314-042927"

    # Set date range
    end_date = datetime.date.today()
    start_date = end_date - datetime.timedelta(days=7)

    print(f"Analyzing costs from {start_date} to {end_date}...")
    filter_query = f'usage_start_time >= "{start_date}T00:00:00Z" AND usage_end_time <= "{end_date}T23:59:59Z"'

    # Retrieve cost breakdown
    try:
        response = billing_client.list_billing_account_usage(
            billing_account_name=billing_account_name,
            filter=filter_query,
        )
        for entry in response:
            print(f"Service: {entry.service_description}, Cost: ${entry.cost}")
    except Exception as e:
        print(f"Error during billing analysis: {e}")

analyze_vertex_ai_costs()
