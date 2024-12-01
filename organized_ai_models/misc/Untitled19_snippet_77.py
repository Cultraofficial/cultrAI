from google.cloud import billing_v1

def test_billing_api():
    try:
        client = billing_v1.CloudBillingClient()
        print("Billing API successfully initialized.")
    except Exception as e:
        print(f"Error initializing Billing API: {e}")

test_billing_api()
