from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Query to retrieve all data from the table
query = """
SELECT *
FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
"""

# Execute the query and fetch results
try:
    query_job = client.query(query)
    print("Querying all data...")
    results = query_job.result()  # Wait for the query to finish

    # Display the data
    for row in results:
        print(row)
except Exception as e:
    print(f"Error querying data: {e}")
