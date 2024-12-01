from google.cloud import aiplatform

aiplatform.init(project="gen-lang-client-0492208227", location="us-central1")

# List active endpoints
endpoints = aiplatform.Endpoint.list()
for endpoint in endpoints:
    print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")
