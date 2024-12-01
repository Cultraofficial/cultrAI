from transformers import AutoModelForSpeechSeq2Seq, AutoTokenizer, AutoModelForCausalLM

# Define model names
whisper_tiny_model_name = "openai/whisper-tiny"
dalle_mini_model_name = "dalle-mini/dalle-mini"

# Download Whisper (Tiny) Model and Tokenizer
print("Downloading Whisper (Tiny) model and tokenizer...")
whisper_tiny_model = AutoModelForSpeechSeq2Seq.from_pretrained(whisper_tiny_model_name, cache_dir="./whisper_tiny_model")
whisper_tiny_tokenizer = AutoTokenizer.from_pretrained(whisper_tiny_model_name, cache_dir="./whisper_tiny_model")
print("Whisper (Tiny) download complete.")

# Download DALL-E Mini Model and Tokenizer
print("Downloading DALL-E Mini model and tokenizer...")
dalle_mini_model = AutoModelForCausalLM.from_pretrained(dalle_mini_model_name, cache_dir="./dalle_mini_model")
dalle_mini_tokenizer = AutoTokenizer.from_pretrained(dalle_mini_model_name, cache_dir="./dalle_mini_model")
print("DALL-E Mini download complete.")
