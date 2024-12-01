def delete_endpoint(endpoint_name):
    print(f"Deleting endpoint: {endpoint_name}")
    endpoints = aiplatform.Endpoint.list(filter=f"display_name={endpoint_name}")
    if endpoints:
        endpoint = endpoints[0]
        endpoint.delete()
        print(f"Deleted endpoint: {endpoint_name}")
    else:
        print(f"Endpoint {endpoint_name} not found.")

# Replace with your endpoint name
delete_endpoint("huggingface-model_endpoint")
