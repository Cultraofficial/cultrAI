def count_table_rows():
    print("Counting the number of rows in the table...")
    try:
        query = f"""
        SELECT COUNT(*) as row_count
        FROM `{project_id}.{dataset_id}.{table_id}`
        """
        query_job = client.query(query)
        for row in query_job:
            print(f"Row count: {row['row_count']}")
    except Exception as e:
        print(f"Error counting rows: {e}")
        raise

count_table_rows()
