from supabase import create_client, Client

# Supabase project details
url = "https://yfzraagzlhizscnklzig.supabase.co"
key = "qxGDWZW_QathL4w_kj9SsMUXCZMBvnMevRim6CGqCCw"  # Service Role Key

# Initialize Supabase client
supabase: Client = create_client(url, key)

# Insert data into the table
try:
    response = supabase.table("test_table").insert({"project_name": "Cultra"}).execute()
    print("Data inserted successfully:", response.data)
except Exception as e:
    print("Error inserting data:", e)
