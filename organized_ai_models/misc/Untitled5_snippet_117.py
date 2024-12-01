from google.cloud import firestore

# Initialize Firestore client
db = firestore.Client()

# Verify connection by adding a sample entry
test_ref = db.collection('system_checks').document('firestore_test')
test_ref.set({
    'status': 'connected',
    'timestamp': firestore.SERVER_TIMESTAMP
})
print("Firestore is successfully connected and ready for data storage.")
