# Import necessary libraries
import os
from google.colab import auth
from google.cloud import storage, aiplatform, firestore

# Authenticate with Google Cloud
auth.authenticate_user()

# Set the Google Application Credentials to access Google Cloud services
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/MyDrive/BrandNewKey.json"
