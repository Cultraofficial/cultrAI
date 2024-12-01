from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM, pipeline

# Model names for top free models
models = {
    "bloom": "bigscience/bloom",  # BLOOM (Large model, advanced NLP capabilities)
    "falcon": "tiiuae/falcon-40b",  # Falcon (High capacity, efficient, NLP capable)
    "t5_xxl": "google/t5-xxl",  # T5-XXL (Versatile, text-to-text, good for task flexibility)
    "llama": "meta-llama/Llama-2-13b",  # LLaMA (Large language model, advanced reasoning)
    "codegeex": "THUDM/CodeGeeX-13B"  # CodeGeeX (Specifically for coding and algorithm generation)
}

# Dictionary to store models and their respective pipelines
model_pipelines = {}

# Function to load a model and create a pipeline
def load_model(model_name, task="text-generation"):
    print(f"Loading {model_name}...")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model_pipelines[model_name] = pipeline(task, model=model, tokenizer=tokenizer)
    print(f"{model_name} loaded successfully.")

# Load each model and create a pipeline
for model_key, model_name in models.items():
    try:
        load_model(model_name)
    except Exception as e:
        print(f"Error loading {model_name}: {e}")

# Function to generate response from a specific model
def generate_response(model_name, prompt, max_length=150):
    if model_name in model_pipelines:
        response = model_pipelines[model_name](prompt, max_length=max_length, num_return_sequences=1)
        return response[0]["generated_text"]
    else:
        return f"Model {model_name} is not loaded."

# Example usage: Generate responses from each model
prompt = "Develop a quantum-inspired algorithm for adaptive storytelling in cinema."
for model_name in model_pipelines.keys():
    print(f"\nResponse from {model_name}:")
    print(generate_response(model_name, prompt))
