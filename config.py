# OAuth Configuration Template
# Copy this file to config.py and fill in your credentials

# Google OAuth Configuration
# Get credentials from: https://console.cloud.google.com/apis/credentials
GOOGLE_CLIENT_ID = "YOUR_GOOGLE_CLIENT_ID"  # Replace with your Google Client ID
GOOGLE_CLIENT_SECRET = "YOUR_GOOGLE_CLIENT_SECRET"  # Replace with your Google Client Secret
GOOGLE_REDIRECT_URI = "http://127.0.0.1:5000/auth/google/callback"

# DigiLocker OAuth Configuration
# Get credentials from: https://digitallocker.gov.in/developer/api/
DIGILOCKER_CLIENT_ID = "YOUR_DIGILOCKER_CLIENT_ID"  # Replace with your DigiLocker Client ID
DIGILOCKER_CLIENT_SECRET = "YOUR_DIGILOCKER_CLIENT_SECRET"  # Replace with your DigiLocker Client Secret
DIGILOCKER_REDIRECT_URI = "http://127.0.0.1:5000/auth/digilocker/callback"

# Session Secret Key (keep this secret in production)
SECRET_KEY = "your-secret-key-change-in-production"
