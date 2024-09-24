import firebase_admin
from firebase_admin import credentials, firestore

# Initialize the Firebase app with the credentials file
cred = credentials.Certificate("./credentials.json")  # Replace with your JSON key file path
firebase_admin.initialize_app(cred)

# Initialize Firestore client
db = firestore.client()

# Function to write data to Firestore
def write_data(collection_name, document_name, data):
    # Reference to the Firestore collection and document
    doc_ref = db.collection(collection_name).document(document_name)
    # Write data to Firestore
    doc_ref.set(data)
    print(f"Data written to {collection_name}/{document_name}")

# Function to read data from Firestore
def read_data(collection_name, document_name):
    # Reference to the Firestore document
    doc_ref = db.collection(collection_name).document(document_name)
    # Fetch the document
    doc = doc_ref.get()
    
    if doc.exists:
        print(f"Document data: {doc.to_dict()}")
        return doc.to_dict()
    else:
        print(f"No document found at {collection_name}/{document_name}")
        return None

# Example usage:
# Data to write
data_to_write = {
    "age": 22,
    "male": True,
    "name": "sankalp"
}

# Writing data to Firestore
write_data("personal_details", "6tsEWOoLqkSJ1qdOiGRB", data_to_write)

# Reading data from Firestore
read_data("personal_details", "6tsEWOoLqkSJ1qdOiGRB")
