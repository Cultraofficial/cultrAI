# Mount Google Drive to access your credentials
from google.colab import drive
drive.mount('/content/drive')

# Install required packages
!pip install google-cloud-storage google-cloud-aiplatform google-auth huggingface_hub transformers

# Import required libraries
from google.cloud import storage
from google.oauth2 import service_account
from huggingface_hub import login

# Define sensitive information
huggingface_token = "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"  # Replace with your Hugging Face token
credentials_path = '/content/drive/My Drive/BrandNewKey.json'  # Replace with your actual file path

# Authenticate Hugging Face
login(huggingface_token)

# Authenticate Google Cloud
try:
    credentials = service_account.Credentials.from_service_account_file(credentials_path)
    print("✅ Google Cloud authentication successful!")
except Exception as e:
    print(f"❌ Google Cloud authentication failed: {e}")

# Function to create a storage bucket
def create_bucket(bucket_name, project_id):
    try:
        client = storage.Client(credentials=credentials, project=project_id)
        bucket = client.create_bucket(bucket_name)
        print(f"✅ Bucket {bucket_name} created successfully!")
    except Exception as e:
        print(f"❌ Failed to create bucket {bucket_name}: {e}")

# Download AI models from Hugging Face
from huggingface_hub import snapshot_download

def download_models(model_list, save_dir="/content/colab_models"):
    for model in model_list:
        try:
            print(f"📦 Downloading model: {model}...")
            snapshot_download(repo_id=model, cache_dir=save_dir)
            print(f"✅ Model {model} downloaded successfully!")
        except Exception as e:
            print(f"❌ Failed to download model {model}: {e}")

# Define the list of AI models to download
ai_models = [
    "EleutherAI/gpt-neo-2.7B",
    "mistralai/Mistral-7B",
    "google/bert-base-uncased",
    "facebook/bart-large"
]

# Main function to execute setup
def main():
    print("🔒 Authenticating and setting up...")

    # Authenticate Hugging Face
    try:
        login(huggingface_token)
        print("✅ Hugging Face authentication successful!")
    except Exception as e:
        print(f"❌ Hugging Face authentication failed: {e}")

    # Authenticate Google Cloud
    try:
        credentials = service_account.Credentials.from_service_account_file(credentials_path)
        print("✅ Google Cloud authentication successful!")
    except Exception as e:
        print(f"❌ Google Cloud authentication failed: {e}")

    # Create a storage bucket
    bucket_name = "cultrai-models-bucket"
    project_id = "gen-lang-client-0492208227"  # Replace with your actual project ID
    create_bucket(bucket_name, project_id)

    # Download AI models
    download_models(ai_models)

# Run the main function
if __name__ == "__main__":
    main()
