# Install required libraries (ensure latest versions)
!pip install pyrebase4 openai==0.28

import pyrebase
import openai
from google.colab import drive

# Mount Google Drive
drive.mount('/content/drive', force_remount=True)

# Firebase configuration
firebase_config = {
    "apiKey": "AIzaSyDuYwf5Z1GyN04cDFeoCalko1X4sOl2zb4",  # Your Firebase API Key
    "authDomain": "cultrai-264f3.firebaseapp.com",  # Firebase Auth Domain
    "databaseURL": "https://cultrai-264f3.firebaseio.com",  # Correct Database URL
    "storageBucket": "cultrai-264f3.appspot.com",  # Firebase Storage Bucket
    "serviceAccount": "/content/drive/My Drive/cultrai-264f3-firebase-adminsdk-b576i-cf12145ca1.json"  # Path to JSON file
}

# Initialize Firebase
try:
    firebase = pyrebase.initialize_app(firebase_config)
    db = firebase.database()
    print("Firebase initialized successfully!")
except Exception as e:
    print("Error initializing Firebase:", e)

# OpenAI API key
openai.api_key = "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"

# Function to insert data into Firebase
def insert_data_to_firebase(data):
    try:
        db.child("projects").push(data)
        print("Data inserted successfully!")
    except Exception as e:
        print("Error inserting data:", e)
        # Provide AI troubleshooting if error occurs
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=f"Explain this Firebase error and suggest a solution: {e}",
                max_tokens=100
            )
            print("AI Suggestion:", response.choices[0].text.strip())
        except Exception as ai_error:
            print("AI Assistance Error:", ai_error)

# Example data to insert
data = {
    "project_name": "Cultra",
    "description": "Interactive storytelling platform"
}

# Insert data into Firebase
insert_data_to_firebase(data)
