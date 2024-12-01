def inspect_table_data():
    print("Inspecting raw data in the table...")
    try:
        query = f"""
        SELECT *
        FROM `{project_id}.{dataset_id}.{table_id}`
        LIMIT 10
        """
        query_job = client.query(query)
        for row in query_job:
            print(row)
    except Exception as e:
        print(f"Error inspecting raw data: {e}")
        raise

# Run the function to inspect table data
inspect_table_data()
