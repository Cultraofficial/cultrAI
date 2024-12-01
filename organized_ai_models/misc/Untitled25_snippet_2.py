# Supabase project details
url = "https://yfzraagzlhizscnklzig.supabase.co"  # Supabase URL
key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlmenJhYWd6bGhpenNjbmtsemlnIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MzIzNzk2MjgsImV4cCI6MjA0Nzk1NTYyOH0.wnGq6qUDW4A76dajKFO4EMUKlJ98KEgsqeDO66Mkjo8"  # Supabase API Key

# Initialize Supabase client
supabase: Client = create_client(url, key)

# Test the connection by creating a sample table and inserting data
try:
    response = supabase.table("test_table").insert({"project_name": "Cultra"}).execute()
    print("Test data inserted successfully:", response.data)
except Exception as e:
    print("Error connecting to Supabase:", e)
