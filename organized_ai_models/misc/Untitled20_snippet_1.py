from google.colab import drive
drive.mount('/content/drive')

!pip install google-cloud-storage google-cloud-aiplatform google-auth

from google.cloud import storage
from google.oauth2 import service_account

credentials_path = '/content/drive/My Drive/BrandNewKey.json'  # Replace with your file path
credentials = service_account.Credentials.from_service_account_file(credentials_path)
