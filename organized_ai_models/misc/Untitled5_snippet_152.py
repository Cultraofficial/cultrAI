import firebase_admin
from firebase_admin import credentials

# Path to your Firebase service account key JSON in Google Drive
cred = credentials.Certificate("/content/drive/My Drive/BrandNewKey.json")
firebase_admin.initialize_app(cred)
