from supabase import create_client, Client

# Supabase project details
url = "https://yfzraagzlhizscnklzig.supabase.co"
service_role_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InlmenJhYWd6bGhpenNjbmtsemlnIiwicm9sZSIsInNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMjM3OTYyOCwiZXhwIjoyMDQ3OTU1NjI4fQ.qxGDWZW_QathL4w_kj9SsMUXCZMBvnMevRim6CGqCCw"  # Service Role Key

# Initialize Supabase client
supabase: Client = create_client(url, service_role_key)

# Insert a test row into 'test_table'
try:
    response = supabase.table("test_table").insert({"project_name": "Cultra"}).execute()
    print("Data inserted successfully:", response.data)
except Exception as e:
    print("Error inserting data:", e)
