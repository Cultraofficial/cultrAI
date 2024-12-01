from google.cloud import bigquery

def analyze_billing():
    # Initialize BigQuery client
    client = bigquery.Client()

    # Billing export table (update with your table ID)
    billing_table = "`your_project_id.billing_export.gcp_billing_table`"

    # Query to analyze costs by service
    query = f"""
        SELECT
            service.description AS service,
            sku.description AS sku,
            SUM(cost) AS total_cost
        FROM {billing_table}
        WHERE cost > 0
        GROUP BY service, sku
        ORDER BY total_cost DESC
        LIMIT 10
    """

    # Execute query
    query_job = client.query(query)
    results = query_job.result()

    print("Top 10 Services by Cost:")
    for row in results:
        print(f"Service: {row.service}, SKU: {row.sku}, Total Cost: ${row.total_cost:.2f}")

# Run the function
analyze_billing()