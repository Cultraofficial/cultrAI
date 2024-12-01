# Firestore entry to track real-time interaction
interaction_ref = db.collection('viewer_interactions').document('sample_interaction')
interaction_ref.set({
    'interaction_type': 'emotion_detection',
    'data': 'happy',
    'timestamp': firestore.SERVER_TIMESTAMP
})
print("Real-time interaction successfully recorded in Firestore.")
