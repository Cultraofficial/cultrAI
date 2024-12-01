from supabase import create_client, Client

# Supabase details
url = "https://yfzraagzlhizscnklzig.supabase.co"
service_role_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInNlcnZpY2Vfcm9sZSIsImlhdCI6MTczMjM3OTYyOCwiZXhwIjoyMDQ3OTU1NjI4fQ.qxGDWZW_QathL4w_kj9SsMUXCZMBvnMevRim6CGqCCw"

supabase: Client = create_client(url, service_role_key)

# Insert a test row
try:
    response = supabase.table("test_table").insert({"project_name": "Cultra"}).execute()
    print("Data inserted successfully:", response.data)
except Exception as e:
    print("Error inserting data:", e)
