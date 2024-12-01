from google.cloud import bigquery

# Automatically extracted project, dataset, and table IDs
project_id = "gen-lang-client-0492208227"  # Your Google Cloud project ID
dataset_id = "billing_export"  # Dataset containing billing data
table_id = "gcp_billing_export"  # Table name for billing export data

# Initialize the BigQuery client
client = bigquery.Client(project=project_id)

# Step 1: Inspect Table Schema
def inspect_table_schema():
    print(f"Inspecting schema for table '{table_id}' in dataset '{dataset_id}'...")
    try:
        table = client.get_table(f"{project_id}.{dataset_id}.{table_id}")
        print("Schema:")
        for schema_field in table.schema:
            print(f"Field: {schema_field.name}, Type: {schema_field.field_type}")
    except Exception as e:
        print(f"Error inspecting schema: {e}")
        raise

# Step 2: Verify Dataset and Table
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

# Step 3: Query Billing Export Data
def query_billing_data():
    print("Querying billing data...")
    try:
        # Updated query to sum costs by available fields (update field names after inspecting schema)
        query = f"""
        SELECT
            service AS service_name,
            usage_start_time,
            SUM(cost) AS total_cost
        FROM
            `{project_id}.{dataset_id}.{table_id}`
        GROUP BY
            service, usage_start_time
        ORDER BY
            total_cost DESC
        LIMIT 10
        """
        query_job = client.query(query)
        print("Query results:")
        for row in query_job:
            print(f"Service: {row['service_name']}, Usage Start: {row['usage_start_time']}, Cost: ${row['total_cost']:.2f}")
    except Exception as e:
        print(f"Error querying billing data: {e}")
        raise

# Step 4: Run the functions
try:
    inspect_table_schema()  # Check the schema first
    verify_dataset_table()
    query_billing_data()
except Exception as e:
    print(f"Process failed: {e}")
