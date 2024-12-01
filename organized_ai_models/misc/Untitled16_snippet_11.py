import os
from transformers import AutoModel, AutoTokenizer

# Mount Google Drive
from google.colab import drive
drive.mount('/content/drive')

# Define the list of models to download
models_to_download = [
    "distilgpt2",
    "distilroberta-base",
    "cardiffnlp/twitter-roberta-base-sentiment",
    "EleutherAI/gpt-neo-125M",
    "deepset/roberta-base-squad2"
]

# Define Google Drive path
save_path = '/content/drive/My Drive/Colab_models'

# Create a log file to track saved models
log_file_path = os.path.join(save_path, 'download_log.txt')

# Check if the log file exists, if not, create it
if not os.path.exists(log_file_path):
    with open(log_file_path, 'w') as f:
        f.write("Download Log:\n")

# Function to log download success or failure
def log_download_status(model_name, status):
    with open(log_file_path, 'a') as f:
        f.write(f"Model: {model_name}, Status: {status}\n")

# Download each model and save to Google Drive
for model_name in models_to_download:
    try:
        print(f"Starting download for model: {model_name}")

        # Load model and tokenizer
        model = AutoModel.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Define model save directory in Google Drive
        model_save_dir = os.path.join(save_path, model_name.replace("/", "_"))
        os.makedirs(model_save_dir, exist_ok=True)

        # Save model and tokenizer
        model.save_pretrained(model_save_dir)
        tokenizer.save_pretrained(model_save_dir)

        print(f"Downloaded and saved: {model_name}")
        log_download_status(model_name, "Success")
    except Exception as e:
        print(f"Failed to download model: {model_name}. Error: {e}")
        log_download_status(model_name, f"Failed - {e}")

print("Download process completed. Check the log file for details.")
