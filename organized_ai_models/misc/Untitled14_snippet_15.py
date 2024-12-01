from google.colab import drive
import os

# Mount Google Drive
drive.mount('/content/drive')

# Specify the directory you want to list (adjust this path if necessary)
directory_path = "/content/drive/My Drive/colab_models"

# Check if the directory exists
if os.path.exists(directory_path):
    # List all files and directories within the specified directory
    print("AI Models in Google Drive (colab_models directory):")
    for root, dirs, files in os.walk(directory_path):
        level = root.replace(directory_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f"{indent}{os.path.basename(root)}/")
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print(f"{subindent}{f}")
else:
    print(f"The specified directory does not exist: {directory_path}")
