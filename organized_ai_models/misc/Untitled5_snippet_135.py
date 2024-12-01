# Adaptive Storytelling Logic
def adapt_story_based_on_interaction(interaction_type, interaction_data):
    """Basic adaptive storytelling function to adjust narrative based on viewer interaction."""
    print(f"Adapting story based on interaction: {interaction_type} with data: {interaction_data}")

    # Example logic: If viewer emotion is 'happy', set the story mood to a positive scene
    if interaction_type == "emotion_detection" and interaction_data == "happy":
        next_scene = "positive_scene"
    elif interaction_type == "emotion_detection" and interaction_data == "sad":
        next_scene = "reflective_scene"
    else:
        next_scene = "neutral_scene"

    # Log the decision in Firestore for tracking
    story_ref = db.collection('story_adaptation').document('current_state')
    story_ref.set({
        'interaction_type': interaction_type,
        'interaction_data': interaction_data,
        'next_scene': next_scene,
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    print(f"Next scene adapted to: {next_scene}")

# Example: Adapt the story based on a viewer's 'happy' emotion
adapt_story_based_on_interaction("emotion_detection", "happy")
