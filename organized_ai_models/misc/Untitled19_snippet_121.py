from google.colab import drive
import shutil
import os

def setup_service_account_key():
    # Mount Google Drive
    print("Mounting Google Drive...")
    drive.mount('/content/drive')

    # Path to the JSON key file in Google Drive
    json_key_in_drive = '/content/drive/My Drive/BrandNewKey.json'

    # Destination path to move the file to the current working directory
    json_key_destination = '/content/BrandNewKey.json'

    try:
        # Copy the file to the current working directory
        print("Copying the JSON key file to the current directory...")
        shutil.copy(json_key_in_drive, json_key_destination)
        print(f"File successfully copied to: {json_key_destination}")

        # Set the environment variable for authentication
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = json_key_destination
        print(f"GOOGLE_APPLICATION_CREDENTIALS set to: {json_key_destination}")
    except FileNotFoundError:
        print(f"Error: JSON key file not found at {json_key_in_drive}. Please ensure the file exists in Google Drive.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Run the setup function
setup_service_account_key()
