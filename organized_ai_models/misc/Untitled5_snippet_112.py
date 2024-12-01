# Path to your service account key file with escape for spaces
SERVICE_ACCOUNT_KEY_PATH = "/content/drive/My\ Drive/BrandNewKey.json"  # Update if necessary

# Alternatively, enclose the entire path in quotes in the gcloud command
!gcloud auth activate-service-account --key-file="${SERVICE_ACCOUNT_KEY_PATH}"
