from google.cloud import bigquery

# Initialize BigQuery client
client = bigquery.Client()

# Define the query to fetch all billing data
query = """
SELECT
    billing_account_id,
    service,
    cost,
    usage_start_time,
    usage_end_time
FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
ORDER BY usage_start_time DESC
LIMIT 100
"""

try:
    # Execute the query
    query_job = client.query(query)
    results = query_job.result()  # Wait for the query to complete

    # Print results in a readable format
    print("Query Results:")
    for row in results:
        print(f"Billing Account ID: {row['billing_account_id']}, "
              f"Service: {row['service']}, "
              f"Cost: ${row['cost']:.2f}, "
              f"Start Time: {row['usage_start_time']}, "
              f"End Time: {row['usage_end_time']}")
except Exception as e:
    # Handle errors
    print(f"Error executing query: {e}")
