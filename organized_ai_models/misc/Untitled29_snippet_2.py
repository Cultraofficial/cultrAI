import requests

# Supabase credentials
SUPABASE_URL = "https://yfzraagzlhizscnklzig.supabase.co"
SUPABASE_KEY = "8f26f34a47c1613c625ca89554d8dc49"
TABLE_NAME = "test_table"

# Function to insert data into Supabase table
def insert_into_supabase(data):
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
    }
    url = f"{SUPABASE_URL}/rest/v1/{TABLE_NAME}"
    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"Data successfully inserted: {data}")
    else:
        print(f"Failed to insert data: {response.text}")

# Example data to insert
data = {
    "id": 1,  # Primary key
    "created_at": "2024-11-24T12:00:00",  # Timestamp example
}

# Insert data into Supabase
insert_into_supabase(data)
