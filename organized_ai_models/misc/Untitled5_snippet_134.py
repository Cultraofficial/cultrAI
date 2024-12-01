# Task Delegation Function
def delegate_task(task_name, parameters):
    """General function to delegate tasks, enabling interaction management and adaptive storytelling."""
    print(f"Delegating task: {task_name} with parameters: {parameters}")
    task_ref = db.collection('tasks').document(task_name)
    task_ref.set({
        'parameters': parameters,
        'status': 'pending',
        'timestamp': firestore.SERVER_TIMESTAMP
    })
    print(f"Task '{task_name}' created in Firestore with status 'pending'.")

# Example: Delegate a task for scene adaptation
delegate_task("scene_adaptation", {"scene_id": "001", "user_profile": "viewer123"})
