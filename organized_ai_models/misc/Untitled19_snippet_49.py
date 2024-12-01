# Set up auto-scaling for endpoints
def setup_auto_scaling(endpoint_name, min_replicas=1, max_replicas=2):
    print(f"Configuring auto-scaling for {endpoint_name}...")
    endpoints = aiplatform.Endpoint.list(filter=f"display_name={endpoint_name}")
    if endpoints:
        endpoint = endpoints[0]
        endpoint.update(min_replica_count=min_replicas, max_replica_count=max_replicas)
        print(f"Auto-scaling set for {endpoint_name}: Min: {min_replicas}, Max: {max_replicas}")
    else:
        print(f"Endpoint {endpoint_name} not found.")

setup_auto_scaling("huggingface-model_endpoint")
