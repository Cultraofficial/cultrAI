import firebase_admin
from firebase_admin import credentials, firestore

# Path to your Firebase service account key JSON
cred = credentials.Certificate("/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()
print("Firebase initialized successfully.")
