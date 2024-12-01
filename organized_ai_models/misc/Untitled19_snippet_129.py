import os

# Set the path to your service account JSON file
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/content/drive/My Drive/BrandNewKey.json"

print("GOOGLE_APPLICATION_CREDENTIALS is set to:", os.environ["GOOGLE_APPLICATION_CREDENTIALS"])
