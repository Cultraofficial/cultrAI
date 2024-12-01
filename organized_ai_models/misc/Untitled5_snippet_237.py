from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os

model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Save model and tokenizer locally
model.save_pretrained("/content/model")
tokenizer.save_pretrained("/content/model")

# Create a .mar file
!torch-model-archiver --model-name {model_name} \
    --version 1.0 \
    --serialized-file /content/model/pytorch_model.bin \
    --handler "text_classification" \
    --extra-files "/content/model/config.json,/content/model/vocab.txt" \
    --export-path /content/model/
