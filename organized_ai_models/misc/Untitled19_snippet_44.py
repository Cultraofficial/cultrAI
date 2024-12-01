from google.colab import drive
import os

# Mount Google Drive to access your service account key
drive.mount('/content/drive')

# Path to your service account key JSON file
SERVICE_ACCOUNT_KEY = "/content/drive/My Drive/BrandNewKey.json"  # Update path if needed

# Authenticate with Google Cloud
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = SERVICE_ACCOUNT_KEY
print("Authenticated with the service account.")
