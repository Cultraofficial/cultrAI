from datetime import datetime, timedelta

def analyze_billing(project_id, dataset_id):
    try:
        client = bigquery.Client(credentials=credentials, project=project_id)
        query = f"""
            SELECT
                service.description AS service,
                SUM(cost) AS total_cost
            FROM `{project_id}.{dataset_id}.gcp_billing_export`
            WHERE usage_start_time >= TIMESTAMP('{(datetime.utcnow() - timedelta(days=7)).isoformat()}')
            GROUP BY service
            ORDER BY total_cost DESC
        """
        results = client.query(query)
        print("Cost Analysis:")
        for row in results:
            print(f"Service: {row['service']}, Cost: ${row['total_cost']:.2f}")
    except Exception as e:
        print(f"Failed to analyze billing: {e}")

analyze_billing(PROJECT_ID, "billing_export")
