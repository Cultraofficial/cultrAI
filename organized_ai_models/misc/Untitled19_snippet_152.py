def query_by_date_range():
    print("Querying data for a specific date range...")
    try:
        query = f"""
        SELECT
            billing_account_id,
            service,
            cost,
            usage_start_time,
            usage_end_time
        FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
        WHERE usage_start_time BETWEEN TIMESTAMP('2024-11-01') AND TIMESTAMP('2024-11-21')
        LIMIT 10
        """
        query_job = client.query(query)
        for row in query_job:
            print(f"Billing Account ID: {row['billing_account_id']}, "
                  f"Service: {row['service']}, Cost: {row['cost']}, "
                  f"Start Time: {row['usage_start_time']}, End Time: {row['usage_end_time']}")
    except Exception as e:
        print(f"Error querying by date range: {e}")
        raise

query_by_date_range()
