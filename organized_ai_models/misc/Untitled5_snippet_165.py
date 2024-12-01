# Import required Firebase Firestore library
from firebase_admin import firestore

# Initialize Firestore client
db = firestore.client()

# Function to add a new document to a specified collection
def add_document(collection_name, document_data, document_id=None):
    if document_id:
        db.collection(collection_name).document(document_id).set(document_data)
    else:
        db.collection(collection_name).add(document_data)
    print(f"Document added to {collection_name} collection.")

# Function to read a document from a specified collection
def get_document(collection_name, document_id):
    doc = db.collection(collection_name).document(document_id).get()
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
        return doc.to_dict()
    else:
        print(f"No document found with ID {document_id} in {collection_name}.")
        return None

# Function to update an existing document
def update_document(collection_name, document_id, updated_data):
    db.collection(collection_name).document(document_id).update(updated_data)
    print(f"Document with ID {document_id} in {collection_name} collection updated.")

# Function to delete a document from a specified collection
def delete_document(collection_name, document_id):
    db.collection(collection_name).document(document_id).delete()
    print(f"Document with ID {document_id} in {collection_name} collection deleted.")
