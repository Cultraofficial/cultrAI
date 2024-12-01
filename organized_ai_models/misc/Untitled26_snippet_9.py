import os
import pyrebase
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive', force_remount=True)

# Define the file name and search for it in Google Drive
file_name = "FireBase.json"
search_folder = "/content/drive/My Drive/"
file_path = None

# Search for the file in the specified folder
for root, dirs, files in os.walk(search_folder):
    for file in files:
        if file == file_name:
            file_path = os.path.join(root, file)
            break

# Check if the file was found
if file_path is None:
    raise FileNotFoundError(f"File '{file_name}' not found in Google Drive. Please ensure it is uploaded.")

print(f"File found: {file_path}")

# Firebase configuration
config = {
    "apiKey": "AIzaSyDuYwf5Z1GyN04cDFeoCalko1X4sOl2zb4",
    "authDomain": "cultrai.firebaseapp.com",
    "databaseURL": "https://cultrai.firebaseio.com",
    "storageBucket": "cultrai.appspot.com",
    "serviceAccount": file_path
}

# Initialize Firebase
try:
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()
    print("Firebase initialized successfully!")
except Exception as e:
    print(f"Error initializing Firebase: {e}")

# Function to insert data
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

# Insert data
insert_data_to_firebase(data)
