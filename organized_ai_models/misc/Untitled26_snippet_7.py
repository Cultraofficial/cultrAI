import pyrebase
import os

# Verify Google Drive is mounted
drive_path = "/content/drive/My Drive/FireBase.json"
if not os.path.exists(drive_path):
    raise FileNotFoundError(f"Firebase key file not found at: {drive_path}")

# Firebase configuration
config = {
    "apiKey": "AIzaSyDuYwf5Z1GyN04cDFeoCalko1X4sOl2zb4",
    "authDomain": "cultrai.firebaseapp.com",
    "databaseURL": "https://cultrai.firebaseio.com",
    "storageBucket": "cultrai.appspot.com",
    "serviceAccount": drive_path  # Automatically detects the file path
}

# Initialize Firebase
firebase = pyrebase.initialize_app(config)
db = firebase.database()

# Function to insert data into Firebase
def insert_data_to_firebase(data):
    try:
        db.child("projects").push(data)
        print("Data inserted successfully!")
    except Exception as e:
        print(f"Error inserting data: {e}")

# Example data to insert
data = {
    "project_name": "cultrAi",
    "description": "A fully AI-driven interactive storytelling project",
    "status": "In Progress"
}

# Insert the data
insert_data_to_firebase(data)
