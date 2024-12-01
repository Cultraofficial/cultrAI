# Mount Google Drive
from google.colab import drive
import os

# Mount Google Drive
drive.mount('/content/drive')

# Define the folder path for models
DRIVE_FOLDER = "/content/drive/My Drive/colab_models/"

# Function to list all files in the specified folder
def list_all_files(folder_path):
    try:
        files = os.listdir(folder_path)
        print(f"Total files in '{folder_path}': {len(files)}")
        for idx, file in enumerate(sorted(files), start=1):
            print(f"{idx}. {file}")
        return sorted(files)  # Sorted list for numerical organization
    except Exception as e:
        print(f"Error accessing folder '{folder_path}': {e}")
        return []

# List and sort all files in the folder
all_files = list_all_files(DRIVE_FOLDER)
