def query_all_billing_data():
    print("Querying all billing data without grouping...")
    try:
        query = f"""
        SELECT
            service,
            billing_account_id,
            cost,
            usage_start_time,
            usage_end_time
        FROM `{project_id}.{dataset_id}.{table_id}`
        LIMIT 10
        """
        query_job = client.query(query)
        print("Query results:")
        for row in query_job:
            print(f"Service: {row['service']}, Billing Account ID: {row['billing_account_id']}, "
                  f"Cost: ${row['cost']:.2f}, Start Time: {row['usage_start_time']}, End Time: {row['usage_end_time']}")
    except Exception as e:
        print(f"Error querying all billing data: {e}")
        raise

# Run the function to query all billing data
query_all_billing_data()
