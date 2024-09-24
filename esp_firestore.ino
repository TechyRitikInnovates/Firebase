#include <Arduino.h>
#include <Firebase_ESP_Client.h>
#include <WiFi.h>
#include <Wire.h>

// Firebase initialization
#include "addons/TokenHelper.h"  // Provide the token generation process info.
#include "addons/FirestoreHelper.h"  // Provide the Firestore payload printing info.

// Initialize Wi-Fi credentials
#define WIFI_SSID "Ritik"
#define WIFI_PASSWORD "8291189618"

// Firebase credentials
#define API_KEY ""
#define DATABASE_URL "https//firebaseio.com"
#define FIRESTORE_URL "https://firestore.googleapis.com/v1/projects/YOUR_PROJECT_ID/databases/(default)/documents"

// Firebase objects
FirebaseData fbdo;
FirebaseAuth auth;
FirebaseConfig config;

// Global Variables
bool signupOK = false;
const int espnum = 101;  // Dummy ESP ID

// Function to initialize WiFi connection
void initWiFi() {
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  Serial.print("Connecting to Wi-Fi");
  while (WiFi.status() != WL_CONNECTED) {
    Serial.print(".");
    delay(300);
  }
  Serial.println();
  Serial.print("Connected with IP: ");
  Serial.println(WiFi.localIP());
}

// Function to initialize Firebase
void initFirebase() {
  config.api_key = API_KEY;
  config.database_url = DATABASE_URL;

  // Sign up to Firebase
  if (Firebase.signUp(&config, &auth, "", "")) {
    Serial.println("Firebase Sign-up OK");
    signupOK = true;
  } else {
    Serial.printf("Sign-up Error: %s\n", config.signer.signupError.message.c_str());
  }

  config.token_status_callback = tokenStatusCallback;  // Firebase Token callback
  Firebase.begin(&config, &auth);
  Firebase.reconnectWiFi(true);
}

// Function to send dummy data to Firestore
void sendDataToFirestore() {
  if (Firebase.ready() && signupOK) {
    String documentPath = "Sensors/ESP" + String(espnum);

    // Create a JSON object to send data
    FirebaseJson json;
    json.set("dummy_int", 123);
    json.set("dummy_float", 45.67);
    json.set("dummy_string", "Hello Firestore!");

    // Send data to Firestore
    if (!Firebase.Firestore.setDocument(&fbdo, documentPath, json)) {
      Serial.println("Failed to send data to Firestore");
      Serial.println("Reason: " + fbdo.errorReason());
    } else {
      Serial.println("Data sent to Firestore successfully.");
    }
  }
}

// Function to read dummy data from Firestore
void readDataFromFirestore() {
  if (Firebase.ready() && signupOK) {
    String documentPath = "Sensors/ESP" + String(espnum);

    // Read data from Firestore
    if (Firebase.Firestore.getDocument(&fbdo, documentPath)) {
      Serial.println("Data retrieved from Firestore:");
      Serial.print("Dummy Int: ");
      Serial.println(fbdo.jsonData().data().at("dummy_int").asInt());
      Serial.print("Dummy Float: ");
      Serial.println(fbdo.jsonData().data().at("dummy_float").asFloat());
      Serial.print("Dummy String: ");
      Serial.println(fbdo.jsonData().data().at("dummy_string").asString());
    } else {
      Serial.println("Failed to get data from Firestore");
      Serial.println("Reason: " + fbdo.errorReason());
    }
  }
}

// Setup function to initialize everything
void setup() {
  Serial.begin(115200);

  // Initialize Wi-Fi
  initWiFi();

  // Initialize Firebase
  initFirebase();
}

// Main loop
void loop() {
  // Send dummy data to Firestore
  sendDataToFirestore();

  // Read dummy data from Firestore
  readDataFromFirestore();

  // Add a delay or condition for periodic checks
  delay(5000);  // Wait for 5 seconds before repeating
}
