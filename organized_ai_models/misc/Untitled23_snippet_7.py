!pip install firebase-admin
import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase service account key JSON
firebase_key_path = "/content/drive/My Drive/BrandNewKey.json"

# Initialize Firebase
cred = credentials.Certificate(firebase_key_path)
firebase_admin.initialize_app(cred)

# Connect to Firestore
db = firestore.client()
print("Firebase Initialized and Connected to Firestore!")
