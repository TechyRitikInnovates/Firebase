import firebase_admin
from firebase_admin import credentials, db, firestore

# Initialize the Firebase app with the credentials file
cred = credentials.Certificate("credentials.json")  # Replace with your JSON key file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://krishi-vikas-8vygft-default-rtdb.firebaseio.com/'  # Replace with your database URL
})

# Initialize Realtime Database client
realtime_ref = db.reference()

# Initialize Firestore client
firestore_db = firestore.client()

# Function to read data from Firebase Realtime Database
def read_data_from_realtime_db(path):
    data = realtime_ref.child(path).get()
    if data:
        print(f"Data read from {path}: {data}")
        return data
    else:
        print(f"No data found at {path}")
        return None

# Function to write data to Firestore
def write_data_to_firestore(collection_name, document_name, data):
    doc_ref = firestore_db.collection(collection_name).document(document_name)
    doc_ref.set(data)
    print(f"Data written to {collection_name}/{document_name}")

# Example usage:
# Path in Realtime Database from which to read data
realtime_data_path = "users/user1"

# Read data from Realtime Database
data_from_realtime_db = read_data_from_realtime_db(realtime_data_path)

if data_from_realtime_db:
    # Path in Firestore where data will be written
    firestore_collection_name = "personal_details"
    firestore_document_name = "6tsEWOoLqkSJ1qdOiGRB"
    
    # Write data to Firestore
    write_data_to_firestore(firestore_collection_name, firestore_document_name, data_from_realtime_db)
