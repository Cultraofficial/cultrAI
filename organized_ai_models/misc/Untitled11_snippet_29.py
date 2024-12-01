service_account_key_path = "/content/drive/My Drive/gitkey.json"

# Authenticate with the Google Cloud SDK
!gcloud auth activate-service-account --key-file="{service_account_key_path}"
!gcloud config set project gen-lang-client-0492208227
