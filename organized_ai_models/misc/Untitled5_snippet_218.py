from google.colab import drive
drive.mount('/content/drive')

# Google Cloud Authentication
!gcloud auth activate-service-account gemini-api-service-account@gen-lang-client-0492208227.iam.gserviceaccount.com --key-file="/content/drive/My Drive/BrandNewKey.json"
!gcloud config set project gen-lang-client-0492208227
