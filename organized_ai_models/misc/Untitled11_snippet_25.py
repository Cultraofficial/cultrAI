from google.colab import drive
drive.mount('/content/drive')

# Specify the full path with quotes to handle spaces in "My Drive"
service_account_path = '/content/drive/My Drive/gitkey.json'

# Authenticate with Google Cloud using the service account key
!gcloud auth activate-service-account --key-file="$service_account_path"

# Set the Google Cloud project
!gcloud config set project gen-lang-client-0492208227
