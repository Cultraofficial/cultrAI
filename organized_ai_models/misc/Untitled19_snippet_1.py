# Mount Google Drive
from google.colab import drive
import os

# Mount Google Drive
drive.mount('/content/drive')

# Specify the folder where models are stored
DRIVE_FOLDER = "/content/drive/My Drive/colab_models/"

# Function to list all files in the specified folder
def list_model_files(folder_path):
    try:
        files = os.listdir(folder_path)
        print(f"Files in '{folder_path}':")
        for file in files:
            print(file)
        return files
    except Exception as e:
        print(f"Error accessing folder '{folder_path}': {e}")
        return []

# List all files in the folder
model_files = list_model_files(DRIVE_FOLDER)
