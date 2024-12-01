from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline

# Define model name
model_name = "bigscience/bloom"

# Deploy BLOOM on Vertex AI
def deploy_bloom():
    print(f"Deploying {model_name} on Vertex AI...")
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        bloom_pipeline = pipeline("text-generation", model=model, tokenizer=tokenizer)
        print(f"{model_name} deployed successfully.")
    except Exception as e:
        print(f"Error deploying {model_name}: {e}")

# Run deployment
deploy_bloom()
