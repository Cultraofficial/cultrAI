from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# Query to retrieve a limited number of rows
query = """
SELECT *
FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
LIMIT 10
"""

# Execute the query and fetch results
try:
    query_job = client.query(query)
    print("Querying limited data...")
    results = query_job.result()  # Wait for the query to finish

    # Display the data
    for row in results:
        print(row)
except Exception as e:
    print(f"Error querying data: {e}")
