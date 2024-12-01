# Query to fetch billing data based on the inspected schema
def query_billing_data_updated():
    print("Querying billing data based on inspected schema...")
    try:
        # Updated query
        query = f"""
        SELECT
            service AS service_name,
            billing_account_id,
            TIMESTAMP_TRUNC(usage_start_time, DAY) AS usage_date,
            SUM(cost) AS total_cost
        FROM
            `{project_id}.{dataset_id}.{table_id}`
        GROUP BY
            service_name, billing_account_id, usage_date
        ORDER BY
            total_cost DESC
        LIMIT 10
        """
        query_job = client.query(query)
        print("Query results:")
        for row in query_job:
            print(f"Service: {row['service_name']}, Billing Account ID: {row['billing_account_id']}, "
                  f"Date: {row['usage_date']}, Cost: ${row['total_cost']:.2f}")
    except Exception as e:
        print(f"Error querying billing data: {e}")
        raise

# Run the updated query function
query_billing_data_updated()
