import shutil

# Define model paths and destination paths
models_to_save = [
    ("./bart_large_model", "/content/drive/My Drive/ModelStorage/bart_large_model"),
    ("./bert_base_model", "/content/drive/My Drive/ModelStorage/bert_base_model"),
    ("./bloom_model", "/content/drive/My Drive/ModelStorage/bloom_model"),
    ("./clip_model", "/content/drive/My Drive/ModelStorage/clip_model"),
    ("./codebert_model", "/content/drive/My Drive/ModelStorage/codebert_model"),
    ("./dalle_mini_model", "/content/drive/My Drive/ModelStorage/dalle_mini_model"),
    ("./distilbert_multilingual_model", "/content/drive/My Drive/ModelStorage/distilbert_multilingual_model"),
    ("./gpt2_large_model", "/content/drive/My Drive/ModelStorage/gpt2_large_model"),
    ("./gpt2_medium_model", "/content/drive/My Drive/ModelStorage/gpt2_medium_model"),
    ("./gpt2_model", "/content/drive/My Drive/ModelStorage/gpt2_model"),
    ("./gpt_j_6b_model", "/content/drive/My Drive/ModelStorage/gpt_j_6b_model"),
    ("./gpt_neox_20b_model", "/content/drive/My Drive/ModelStorage/gpt_neox_20b_model"),
    ("./stable_diffusion_model", "/content/drive/My Drive/ModelStorage/stable_diffusion_model"),
    ("./t5_large_model", "/content/drive/My Drive/ModelStorage/t5_large_model"),
    ("./whisper_tiny_model", "/content/drive/My Drive/ModelStorage/whisper_tiny_model")
]

# Move each model directory to Google Drive
for src, dest in models_to_save:
    try:
        shutil.move(src, dest)
        print(f"{src.split('/')[-1]} saved to Google Drive.")
    except FileNotFoundError:
        print(f"Error: {src.split('/')[-1]} not found.")
