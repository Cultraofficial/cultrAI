# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Set the path to the BrandNewKey.json file
service_account_path = '/content/drive/My Drive/BrandNewKey.json'

# Initialize Firebase connection
import firebase_admin
from firebase_admin import credentials

try:
    # Load the service account credentials
    cred = credentials.Certificate(service_account_path)
    firebase_admin.initialize_app(cred)
    print("Firebase successfully connected.")
except Exception as e:
    print(f"Firebase connection error: {e}")
