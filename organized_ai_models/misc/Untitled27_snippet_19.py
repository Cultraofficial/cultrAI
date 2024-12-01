import requests
import pyrebase

# Firebase Configuration (Automatically Applied)
firebase_config = {
    "apiKey": "AIzaSyDuYwf5Z1GyN04cDFeoCalko1X4sOl2zb4",  # Automatically applied API Key
    "authDomain": "cultrai-264f3.firebaseapp.com",
    "databaseURL": "https://cultrai-264f3-default-rtdb.firebaseio.com",
    "storageBucket": "cultrai-264f3.appspot.com",
}

def fetch_and_store(api_url, firebase_config):
    """
    Fetch data from an API and store it in Firebase Realtime Database.

    :param api_url: The API endpoint to fetch data from.
    :param firebase_config: Firebase configuration dictionary.
    """
    try:
        # Initialize Firebase
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()

        # Fetch data from API
        print("Fetching data from API...")
        response = requests.get(api_url)

        # Check for errors
        if response.status_code != 200:
            print(f"Error: Failed to fetch data. Status code: {response.status_code}")
            return

        data = response.json()  # Parse JSON response

        # Store data in Firebase
        print("Storing data in Firebase...")
        db.child("api_data").set(data)  # Replace 'api_data' with your desired path
        print("Data successfully stored in Firebase!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Example API endpoint
fetch_and_store(api_url, firebase_config)
