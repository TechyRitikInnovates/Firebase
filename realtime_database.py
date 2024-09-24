import firebase_admin
from firebase_admin import credentials, db

# Initialize the Firebase app with the credentials file
cred = credentials.Certificate("credentials.json")  # Replace with your JSON key file path
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://firebaseio.com/'  # Replace with your database URL
})

# Initialize Realtime Database client
ref = db.reference()

# Function to write data to Firebase Realtime Database
def write_data(path, data):
    # Reference to the path where data will be written
    ref.child(path).set(data)
    print(f"Data written to {path}")

# Function to read data from Firebase Realtime Database
def read_data(path):
    # Reference to the path where data will be read from
    data = ref.child(path).get()
    if data:
        print(f"Data read from {path}: {data}")
    else:
        print(f"No data found at {path}")
    return data

# Example usage:
# Data to write
data_to_write = {
    "age": 20,
    "male": True,
    "name": "ritik"
}

# Write data to Realtime Database
write_data("users/user1", data_to_write)

# Read data from Realtime Database
read_data("users/user1")
