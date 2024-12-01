import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin
cred = credentials.Certificate('/content/drive/My Drive/BrandNewKey.json')  # Update with your path
try:
    firebase_admin.initialize_app(cred)
except ValueError:
    # Avoid re-initialization error if Firebase was already initialized
    pass

db = firestore.client()

# Function to add test user data
def add_test_user():
    user_data = {
        "username": "test_user",
        "email": "test@example.com",
        "interaction_count": 0
    }
    db.collection("users").document("test_user").set(user_data)
    print("Test user added to Firestore.")

# Function to retrieve and display user data
def get_user_data():
    doc_ref = db.collection("users").document("test_user")
    doc = doc_ref.get()
    if doc.exists:
        print(f"User data: {doc.to_dict()}")
    else:
        print("No user data found.")

# Run test functions
add_test_user()
get_user_data()
