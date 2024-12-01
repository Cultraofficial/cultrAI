from transformers import AutoModelForCausalLM, AutoTokenizer
from diffusers import StableDiffusionPipeline

# Define model names
whisper_tiny_model_name = "openai/whisper-tiny"
stable_diffusion_model_name = "CompVis/stable-diffusion-v1-4"  # Alternative to DALL-E Mini

# Download Whisper (Tiny) Model and Tokenizer
print("Downloading Whisper (Tiny) model and tokenizer...")
whisper_tiny_model = AutoModelForSpeechSeq2Seq.from_pretrained(whisper_tiny_model_name, cache_dir="./whisper_tiny_model")
whisper_tiny_tokenizer = AutoTokenizer.from_pretrained(whisper_tiny_model_name, cache_dir="./whisper_tiny_model")
print("Whisper (Tiny) download complete.")

# Download Stable Diffusion Model for Image Generation
print("Downloading Stable Diffusion model and pipeline...")
stable_diffusion = StableDiffusionPipeline.from_pretrained(stable_diffusion_model_name, cache_dir="./stable_diffusion_model")
print("Stable Diffusion download complete.")
