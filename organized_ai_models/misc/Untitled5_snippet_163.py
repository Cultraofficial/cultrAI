# Import necessary libraries
import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin with your service account key
cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Adjust the path if necessary
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()
print("Firebase and Firestore initialized.")
