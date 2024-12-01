import os

# Create a new folder in Google Drive
new_folder_path = '/content/drive/My Drive/CultrA.I. Files'
os.makedirs(new_folder_path, exist_ok=True)

print(f"Folder created at: {new_folder_path}")
