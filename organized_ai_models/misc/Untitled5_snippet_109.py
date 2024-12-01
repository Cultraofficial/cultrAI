# Path with escaped spaces for service account key
SERVICE_ACCOUNT_KEY_PATH = "/content/drive/My\ Drive/BrandNewKey.json"

# Activate the service account
!gcloud auth activate-service-account --key-file=$SERVICE_ACCOUNT_KEY_PATH
