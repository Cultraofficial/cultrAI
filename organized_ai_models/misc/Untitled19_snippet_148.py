def get_table_schema():
    print("Fetching table schema...")
    try:
        table = client.get_table(f"{project_id}.{dataset_id}.{table_id}")
        for field in table.schema:
            print(f"Field: {field.name}, Type: {field.field_type}")
    except Exception as e:
        print(f"Error fetching table schema: {e}")
        raise

get_table_schema()
