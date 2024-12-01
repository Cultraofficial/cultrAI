# Define your bucket name
BUCKET_NAME = 'cultra_official'

# Initialize the Google Cloud Storage client
client = storage.Client()
bucket = client.get_bucket(BUCKET_NAME)

# Define folder structure in Colab to match Vertex
folders = [
    'platform',  # Core codebase for the interactive platform
    'data',  # Folder for datasets
    'models',  # Folder for model checkpoints and trained models
    'logs',  # Folder for logging and tracking AI processes
]

# Create the folder structure in Colab
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"Folder created: {folder}")
