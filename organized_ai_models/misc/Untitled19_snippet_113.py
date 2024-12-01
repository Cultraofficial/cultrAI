from google.cloud import bigquery

def create_billing_export_table(project_id, dataset_id):
    try:
        client = bigquery.Client()
        dataset_ref = bigquery.Dataset(f"{project_id}.{dataset_id}")
        table_id = "gcp_billing_export"
        schema = [
            bigquery.SchemaField("billing_account_id", "STRING"),
            bigquery.SchemaField("service", "STRING"),
            bigquery.SchemaField("cost", "FLOAT"),
            bigquery.SchemaField("usage_start_time", "TIMESTAMP"),
            bigquery.SchemaField("usage_end_time", "TIMESTAMP"),
        ]
        table_ref = bigquery.Table(dataset_ref.table(table_id), schema=schema)
        table = client.create_table(table_ref)
        print(f"Table {table.table_id} created successfully.")
    except Exception as e:
        print(f"Failed to create BigQuery table: {e}")

create_billing_export_table(PROJECT_ID, "billing_export")
