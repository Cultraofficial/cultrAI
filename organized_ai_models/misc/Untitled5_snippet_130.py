# Verify Firestore connection
def verify_firestore_connection():
    try:
        test_ref = db.collection('system_checks').document('firestore_test')
        test_ref.set({
            'status': 'connected',
            'timestamp': firestore.SERVER_TIMESTAMP
        })
        print("Firestore connection verified.")
    except Exception as e:
        print("Firestore verification failed:", e)

verify_firestore_connection()

# List contents of a specific bucket folder to verify Storage access
def list_bucket_contents(bucket_name, folder_prefix):
    """List contents in the specified Google Cloud Storage bucket folder."""
    try:
        bucket = storage_client.get_bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=folder_prefix)
        for blob in blobs:
            print(blob.name)
        print("Google Cloud Storage access verified.")
    except Exception as e:
        print("Storage verification failed:", e)

# Replace 'cultra_official' with your actual bucket name and 'platform' with folder prefix
list_bucket_contents('cultra_official', 'platform')
