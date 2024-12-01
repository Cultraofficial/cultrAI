def automate_cost_monitoring():
    try:
        from google.cloud import monitoring_v3

        client = monitoring_v3.AlertPolicyServiceClient()
        project_name = f"projects/{PROJECT_ID}"

        alert_policy = monitoring_v3.AlertPolicy(
            display_name="High Billing Alert",
            conditions=[
                monitoring_v3.AlertPolicy.Condition(
                    display_name="Billing exceeds threshold",
                    condition_threshold=monitoring_v3.AlertPolicy.Condition.MetricThreshold(
                        filter="metric.type=\"billing.googleapis.com/billing/account/actual_spend\"",
                        comparison=monitoring_v3.ComparisonType.COMPARISON_GT,
                        threshold_value=100.0,  # Adjust threshold as needed
                    )
                )
            ]
        )
        client.create_alert_policy(name=project_name, alert_policy=alert_policy)
        print("Automated cost monitoring set up successfully!")
    except Exception as e:
        print(f"Failed to set up cost monitoring: {e}")

automate_cost_monitoring()
