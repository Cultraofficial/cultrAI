from google.colab import drive
import os

# Mount Google Drive
drive.mount('/content/drive')

# Define paths to both folders
folder_path_1 = '/content/drive/My Drive/Colab_models'
folder_path_2 = '/content/drive/My Drive/colab_models'

# Function to list contents of a folder
def list_folder_contents(folder_path):
    if os.path.exists(folder_path):
        print(f"Contents of {folder_path}:")
        for file_name in os.listdir(folder_path):
            print(file_name)
    else:
        print(f"Folder {folder_path} does not exist.")

# Check both folders
list_folder_contents(folder_path_1)
list_folder_contents(folder_path_2)
