from google.colab import drive
import os

# Mount Google Drive
drive.mount('/content/drive')

# Define the path to your 'colab_models' directory
directory_path = "/content/drive/My Drive/colab_models"

# Check if the directory exists and list contents
if os.path.exists(directory_path):
    print("Listing all files and folders in 'colab_models':\n")
    for item in os.listdir(directory_path):
        print(item)
else:
    print(f"The specified directory does not exist: {directory_path}")
