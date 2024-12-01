import psycopg2
from psycopg2 import sql

# Supabase credentials
HOST = "yfzraagzlhizscnklzig.supabase.co"  # Supabase host
DATABASE = "postgres"                     # Default database name for Supabase
USER = "postgres"                         # Default username for Supabase
PASSWORD = "212cb29a93678cb12e3711ad1315de7d58321342440b04fcaa91f5f733bebe9c"  # Supabase database password
PORT = 5432                               # Default Postgres port

try:
    # Connect to the Supabase database
    print("Connecting to Supabase...")
    conn = psycopg2.connect(
        host=HOST,
        database=DATABASE,
        user=USER,
        password=PASSWORD,
        port=PORT
    )
    cursor = conn.cursor()

    # Create a table to store API data
    print("Creating table 'api_data' if it doesn't exist...")
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS api_data (
        id SERIAL PRIMARY KEY,
        data JSONB NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)
    conn.commit()
    print("Table 'api_data' created successfully!")

    # Insert a sample JSON record
    print("Inserting sample data into 'api_data'...")
    sample_data = {"message": "Hello from Supabase!"}
    cursor.execute(
        sql.SQL("INSERT INTO api_data (data) VALUES (%s)"),
        [json.dumps(sample_data)]
    )
    conn.commit()
    print("Sample data inserted successfully!")

    # Fetch and display data from the table
    print("Fetching data from 'api_data'...")
    cursor.execute("SELECT * FROM api_data")
    rows = cursor.fetchall()
    for row in rows:
        print(f"Row {row[0]}: {row[1]} - Created at {row[2]}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
    print("Database connection closed.")
