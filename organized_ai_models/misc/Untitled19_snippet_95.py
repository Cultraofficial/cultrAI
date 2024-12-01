from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
import os

# Authenticate with additional scopes
SCOPES = ["https://www.googleapis.com/auth/cloud-platform", "https://www.googleapis.com/auth/cloud-billing"]
CREDENTIALS_FILE = "/content/drive/My Drive/BrandNewKey.json"

credentials = Credentials.from_service_account_file(CREDENTIALS_FILE, scopes=SCOPES)
credentials.refresh(Request())

print("Authenticated successfully with additional scopes.")
