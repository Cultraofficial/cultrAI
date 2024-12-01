from google.colab import drive
import os

# Mount Google Drive
drive.mount('/content/drive')

# Path to your service account key file
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Replace with the correct path

# Authenticate with Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
print("Authenticated with the service account.")
