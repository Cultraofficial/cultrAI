# Mount Google Drive
from google.colab import drive
import os
import requests
import pyrebase
import time
import schedule

print("Mounting Google Drive...")
drive.mount('/content/drive')

# Set up project folder
project_folder = "/content/drive/My Drive/CultrA.I. Files"
os.makedirs(project_folder, exist_ok=True)
print(f"Project folder ready at: {project_folder}")

# Firebase Configuration
firebase_config = {
    "apiKey": "YOUR_FIREBASE_API_KEY",
    "authDomain": "YOUR_FIREBASE_PROJECT.firebaseapp.com",
    "databaseURL": "https://YOUR_FIREBASE_PROJECT.firebaseio.com",
    "storageBucket": "YOUR_FIREBASE_PROJECT.appspot.com"
}

# Initialize Firebase
try:
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    print("Firebase initialized successfully!")
except Exception as e:
    print(f"Error initializing Firebase: {e}")
    raise

# Function to fetch data from an API and store it in Firebase
def fetch_and_store(api_url, firebase_node):
    try:
        # Fetch data from the API
        print(f"Fetching data from API: {api_url}...")
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Store data in Firebase
        print(f"Storing data in Firebase under node '{firebase_node}'...")
        db.child(firebase_node).set(data)
        print(f"Data successfully stored in Firebase under node '{firebase_node}'!")

        # Back up data to Google Drive
        backup_file = os.path.join(project_folder, f"{firebase_node}_backup.json")
        with open(backup_file, "w") as file:
            file.write(str(data))
        print(f"Data successfully backed up to Google Drive at: {backup_file}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Scheduler Job
def job():
    # List of API endpoints to fetch data from
    api_urls = [
        "https://jsonplaceholder.typicode.com/todos/1",  # Test API 1
        "https://jsonplaceholder.typicode.com/todos/2"   # Test API 2
    ]

    # Loop through API URLs and store data
    for i, api_url in enumerate(api_urls, start=1):
        firebase_node = f"api_data_{i}"  # Node name in Firebase
        fetch_and_store(api_url, firebase_node)

# Set up the scheduler to run every 10 minutes
schedule.every(10).minutes.do(job)

# Start the scheduler
print("Starting the scheduler...")
while True:
    schedule.run_pending()
    time.sleep(1)
