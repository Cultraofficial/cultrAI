import os
from google.oauth2.service_account import Credentials

# Correct path to the JSON file
credentials_path = "/content/drive/My Drive/BrandNewKey.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

# Load credentials
credentials = Credentials.from_service_account_file(credentials_path)

print("Credentials loaded successfully!")
