from google.cloud import bigquery

# Initialize the BigQuery client
client = bigquery.Client()

# List datasets in your project
datasets = list(client.list_datasets())
if datasets:
    print("Datasets in project:")
    for dataset in datasets:
        print(f" - {dataset.dataset_id}")
else:
    print("No datasets found.")
