import os

# Define the path where models are stored
drive_path = '/content/drive/My Drive/Colab_models/'

# Check if the path exists
if os.path.exists(drive_path):
    print(f"Contents of {drive_path}:")
    # Walk through the directory and list files
    for root, dirs, files in os.walk(drive_path):
        for name in files:
            print(os.path.join(root, name))
else:
    print(f"The directory {drive_path} does not exist.")
