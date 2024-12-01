os.environ["HF_TOKEN"] = "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"

from huggingface_hub import login
login(os.getenv("HF_TOKEN"))
