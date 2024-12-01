def count_rows():
    print("Counting total rows in the table...")
    try:
        query = f"""
        SELECT COUNT(*) as total_rows
        FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
        """
        query_job = client.query(query)
        for row in query_job:
            print(f"Total rows: {row['total_rows']}")
    except Exception as e:
        print(f"Error counting rows: {e}")
        raise

count_rows()
