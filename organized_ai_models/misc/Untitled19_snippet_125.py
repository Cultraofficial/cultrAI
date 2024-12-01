try:
    from google.cloud import bigquery, logging_v2, monitoring_v3, billing_v1, resourcemanager_v3
    from google.auth.exceptions import DefaultCredentialsError
    from google.api_core.exceptions import GoogleAPIError
    import os
except ImportError as e:
    print(f"Required library is missing: {e}")
    print("Run the following command to install all necessary dependencies:")
    print("!pip install --upgrade google-cloud-bigquery google-cloud-monitoring google-cloud-billing google-cloud-logging google-cloud-resourcemanager")
    raise
