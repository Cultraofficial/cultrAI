from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Google Cloud Authentication (automatically detects the account from JSON key file)
!gcloud auth activate-service-account --key-file="/content/drive/My Drive/BrandNewKey.json"
!gcloud config set project gen-lang-client-0492208227
