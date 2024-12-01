import json

# Path to your JSON key file
json_key_file = "/content/drive/My Drive/BrandNewKey.json"  # Update path if necessary

# Load and display the client_email
with open(json_key_file, "r") as file:
    key_data = json.load(file)
    print("Service Account Email:", key_data["client_email"])
