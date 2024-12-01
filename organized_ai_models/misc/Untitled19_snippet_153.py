def query_all_data():
    print("Querying all data to inspect available records...")
    try:
        query = """
        SELECT
            billing_account_id,
            service,
            cost,
            usage_start_time,
            usage_end_time
        FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
        ORDER BY usage_start_time ASC
        LIMIT 20
        """
        query_job = client.query(query)
        print("Query results:")
        for row in query_job:
            print(f"Billing Account ID: {row['billing_account_id']}, "
                  f"Service: {row['service']}, Cost: {row['cost']}, "
                  f"Start Time: {row['usage_start_time']}, End Time: {row['usage_end_time']}")
    except Exception as e:
        print(f"Error querying all data: {e}")

query_all_data()
