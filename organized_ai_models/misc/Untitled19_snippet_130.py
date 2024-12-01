from google.cloud import bigquery, monitoring_v3
from google.oauth2.service_account import Credentials

# Load the service account credentials
credentials_path = "/content/drive/My Drive/BrandNewKey.json"
credentials = Credentials.from_service_account_file(credentials_path)

# Initialize clients with explicit credentials
bigquery_client = bigquery.Client(credentials=credentials)
monitoring_client = monitoring_v3.MetricServiceClient(credentials=credentials)

print("Clients initialized with explicit credentials!")
