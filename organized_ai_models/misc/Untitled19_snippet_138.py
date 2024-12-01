from google.cloud import bigquery

# Automatically extracted project, dataset, and table IDs
project_id = "gen-lang-client-0492208227"  # Your Google Cloud project ID
dataset_id = "billing_export"  # Dataset containing billing data
table_id = "gcp_billing_export"  # Table name for billing export data

# Initialize the BigQuery client
client = bigquery.Client(project=project_id)

# Step 1: Verify Dataset and Table
def verify_dataset_table():
    print(f"Verifying dataset '{dataset_id}' and table '{table_id}' in project '{project_id}'...")
    try:
        # List tables in the dataset
        tables = client.list_tables(f"{project_id}.{dataset_id}")
        table_exists = any(table.table_id == table_id for table in tables)
        if table_exists:
            print(f"Dataset and table verified: {project_id}.{dataset_id}.{table_id}")
        else:
            raise Exception(f"Table '{table_id}' not found in dataset '{dataset_id}'.")
    except Exception as e:
        print(f"Error verifying dataset or table: {e}")
        raise

# Step 2: Query Billing Export Data
def query_billing_data():
    print("Querying billing data...")
    try:
        query = f"""
        SELECT
            project.id AS project_id,
            SUM(cost) AS total_cost
        FROM
            `{project_id}.{dataset_id}.{table_id}`
        GROUP BY
            project_id
        ORDER BY
            total_cost DESC
        LIMIT 10
        """
        query_job = client.query(query)
        print("Query results:")
        for row in query_job:
            print(f"Project: {row['project_id']}, Cost: ${row['total_cost']:.2f}")
    except Exception as e:
        print(f"Error querying billing data: {e}")
        raise

# Step 3: Run the functions
try:
    verify_dataset_table()
    query_billing_data()
except Exception as e:
    print(f"Process failed: {e}")
