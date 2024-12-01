import os

# Define the directory path
save_directory = '/content/drive/My Drive/downloaded_models'

# Create the directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

print(f"Models will be saved in: {save_directory}")
