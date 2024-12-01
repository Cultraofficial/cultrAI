import os

from google.colab import drive
drive.mount('/content/drive', force_remount=True)

# Search for the file in Google Drive
search_folder = "/content/drive/My Drive/"
file_name = "FireBase.json"  # Update with your exact file name if different
file_path = None

for root, dirs, files in os.walk(search_folder):
    if file_name in files:
        file_path = os.path.join(root, file_name)
        break

if file_path is None:
    raise FileNotFoundError(f"File '{file_name}' not found in Google Drive!")

print(f"File found: {file_path}")
