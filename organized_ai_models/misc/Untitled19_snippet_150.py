def fetch_table_content():
    print("Fetching the first 10 rows from the table...")
    try:
        query = f"""
        SELECT *
        FROM `gen-lang-client-0492208227.billing_export.gcp_billing_export`
        LIMIT 10
        """
        query_job = client.query(query)
        for row in query_job:
            print(row)
    except Exception as e:
        print(f"Error fetching table content: {e}")
        raise

fetch_table_content()
