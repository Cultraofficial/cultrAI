import os

# Set the path to the service account key
service_account_path = '/content/drive/My Drive/gitkey.json'

# Authenticate with Google Cloud
!gcloud auth activate-service-account --key-file={service_account_path}

# Set the project ID (make sure this is correct)
!gcloud config set project gen-lang-client-0492208227
