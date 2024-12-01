# Example: Query BigQuery table
query = """
SELECT
    project.id AS project_id,
    SUM(cost) AS total_cost
FROM
    `project_id.billing_export.gcp_billing_export`
GROUP BY
    project_id
ORDER BY
    total_cost DESC
LIMIT 10
"""
query_job = client.query(query)
for row in query_job:
    print(f"Project: {row['project_id']}, Cost: {row['total_cost']}")
