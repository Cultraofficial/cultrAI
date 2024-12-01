import time

def auto_save():
    # Periodic save to Firestore for state persistence
    status_ref = db.collection('system_checks').document('gemini_status')
    status_ref.set({
        'status': 'working',
        'last_save': firestore.SERVER_TIMESTAMP
    })
    print("Gemini state saved successfully.")

# Example periodic save loop (run asynchronously in practice)
for _ in range(10):  # Replace with actual loop control
    auto_save()
    time.sleep(90)  # Save every 90 seconds
