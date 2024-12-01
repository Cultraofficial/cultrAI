# Remaining models to download, ordered by size
next_models_to_download = [
    "google/t5-small",
    "google/pegasus-cnn-dailymail",
    "facebook/m2m100-418M",
    # Add additional models from your list here if required
]

# Download the next set of models
for model_name in next_models_to_download:
    download_and_save_model(model_name)
