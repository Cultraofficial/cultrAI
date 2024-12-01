import psycopg2

# Supabase credentials
conn = psycopg2.connect(
    host="YOUR_SUPABASE_HOST",
    database="YOUR_DATABASE_NAME",
    user="YOUR_USER",
    password="YOUR_PASSWORD",
    port=5432
)
cursor = conn.cursor()

# Create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS api_data (
    id SERIAL PRIMARY KEY,
    data JSONB NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")
conn.commit()
print("Database ready!")
