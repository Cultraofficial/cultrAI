from google.cloud import firestore
import google.auth

# Explicitly set the project ID
project_id = "your_actual_project_id"  # Replace with your actual project ID
credentials, _ = google.auth.default()

# Initialize Firestore with the explicit project ID
db = firestore.Client(project=project_id, credentials=credentials)

# Verify Firestore connection
def verify_firestore_connection():
    test_ref = db.collection('system_checks').document('firestore_test')
    test_ref.set({
        'status': 'connected',
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    print("Firestore connection verified and test entry added.")

verify_firestore_connection()
