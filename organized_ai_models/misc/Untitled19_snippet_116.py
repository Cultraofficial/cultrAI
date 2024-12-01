from google.cloud import monitoring_v3

def setup_cost_monitoring(project_id):
    try:
        client = monitoring_v3.DashboardsServiceClient()

        # Define the dashboard
        dashboard = {
            "display_name": "Cloud Billing Dashboard",
            "grid_layout": {
                "columns": 2,
                "widgets": [
                    {
                        "title": "Billing Costs",
                        "xy_chart": {
                            "data_sets": [
                                {
                                    "time_series_query": {
                                        "time_series_filter": {
                                            "filter": 'metric.type="billing.gcp.cumulative_cost"',
                                            "aggregation": {
                                                "alignment_period": "3600s",
                                                "per_series_aligner": "ALIGN_SUM",
                                            },
                                        }
                                    },
                                    "target_axis": "Y1",
                                }
                            ],
                            "timeshift_duration": "0s",
                        },
                    }
                ],
            },
        }

        # Create the dashboard
        parent = f"projects/{project_id}"
        response = client.create_dashboard(parent=parent, dashboard=dashboard)
        print(f"Dashboard created successfully: {response.name}")
    except Exception as e:
        print(f"Failed to set up cost monitoring: {e}")

setup_cost_monitoring("your-project-id")
