# List available Vertex AI models to verify access
models = aiplatform.Model.list()
print("Available Vertex AI models:")
for model in models:
    print(model.display_name)
