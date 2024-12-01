import pyrebase

firebase_config = {
    "apiKey": "AIzaSyDuYwf5Z1GyN04cDFeoCalko1X4sOl2zb4",  # Updated API key
    "authDomain": "cultrai-264f3.firebaseapp.com",
    "databaseURL": "https://cultrai-264f3-default-rtdb.firebaseio.com",
    "storageBucket": "cultrai-264f3.appspot.com",
}

# Initialize Firebase
firebase = pyrebase.initialize_app(firebase_config)
db = firebase.database()

# Test Firebase
try:
    print("Testing Firebase...")
    db.child("test").set({"status": "working"})
    print("Firebase is successfully configured!")
except Exception as e:
    print(f"Firebase error: {e}")
