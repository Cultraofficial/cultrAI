from google.colab import drive
drive.mount('/content/drive', force_remount=True)

!gcloud auth activate-service-account --key-file="/content/drive/My Drive/BrandNewKey.json"
