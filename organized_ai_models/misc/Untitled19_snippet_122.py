# Importing required libraries
from google.cloud import bigquery, monitoring_v3
from google.cloud.monitoring_v3 import AlertPolicyServiceClient, NotificationChannelServiceClient
from google.protobuf.duration_pb2 import Duration
import os

# Authenticate with your Google Cloud service account
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/path/to/your/service-account.json"  # Update the path

# Initialize clients
bigquery_client = bigquery.Client()
monitoring_client = monitoring_v3.MetricServiceClient()
alert_client = AlertPolicyServiceClient()
notification_client = NotificationChannelServiceClient()

# Define BigQuery project, dataset, and table
PROJECT_ID = "gen-lang-client-0492208227"
DATASET_ID = "billing_export"
TABLE_ID = "gcp_billing_export"

# BigQuery: Query billing data
def query_billing_data():
    query = f"""
        SELECT
            service.description AS service_name,
            SUM(cost) AS total_cost,
            EXTRACT(DATE FROM usage_start_time) AS date
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        WHERE cost > 0
        GROUP BY service_name, date
        ORDER BY total_cost DESC
        LIMIT 10
    """
    print("Querying BigQuery billing data...")
    query_job = bigquery_client.query(query)
    results = query_job.result()
    print("Billing Data:")
    for row in results:
        print(f"Service: {row.service_name}, Cost: {row.total_cost}, Date: {row.date}")

# Cloud Monitoring: Create alert policy
def create_alert_policy():
    print("Creating Cloud Monitoring Alert Policy...")
    project_name = f"projects/{PROJECT_ID}"
    notification_channels = list(notification_client.list_notification_channels(request={"name": project_name}))
    if not notification_channels:
        print("No notification channels found. Please set up an email or Slack channel in Monitoring.")
        return

    notification_channel = notification_channels[0].name
    policy = monitoring_v3.AlertPolicy(
        display_name="High Billing Alert",
        conditions=[
            monitoring_v3.AlertPolicy.Condition(
                display_name="Cost exceeds $500",
                condition_threshold=monitoring_v3.AlertPolicy.Condition.MetricThreshold(
                    filter='metric.type="billing.googleapis.com/billing/cost/actual_cost"',
                    comparison=monitoring_v3.ComparisonType.COMPARISON_GT,
                    threshold_value=500,
                    duration=Duration(seconds=3600),  # 1 hour
                    aggregations=[
                        monitoring_v3.Aggregation(
                            alignment_period=Duration(seconds=3600),
                            per_series_aligner=monitoring_v3.Aggregation.Aligner.ALIGN_SUM,
                        )
                    ],
                ),
            )
        ],
        notification_channels=[notification_channel],
        combiner=monitoring_v3.AlertPolicy.ConditionCombinerType.AND,
        enabled=True,
    )

    alert_policy = alert_client.create_alert_policy(
        request={"name": project_name, "alert_policy": policy}
    )
    print(f"Alert Policy created: {alert_policy.name}")

# BigQuery: Optimize billing resources
def optimize_resources():
    print("Optimizing resource usage...")
    query = f"""
        SELECT
            service.description AS service_name,
            SUM(cost) AS total_cost
        FROM `{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}`
        WHERE cost > 0
        GROUP BY service_name
        ORDER BY total_cost DESC
        LIMIT 5
    """
    query_job = bigquery_client.query(query)
    results = query_job.result()

    print("Top 5 costliest services:")
    for row in results:
        print(f"Service: {row.service_name}, Cost: {row.total_cost}")

    # Add optimization recommendations
    print("\nRecommendations:")
    print("1. Reduce instance sizes for high-cost services.")
    print("2. Use sustained-use discounts or preemptible instances for Compute Engine.")
    print("3. Decrease storage usage or switch to Nearline/Coldline for low-access data.")
    print("4. Shut down unused resources.")

# Main function to run all tasks
def main():
    print("Starting automated billing analysis and optimization...")
    query_billing_data()
    create_alert_policy()
    optimize_resources()
    print("Automation complete!")

# Run the script
if __name__ == "__main__":
    main()
