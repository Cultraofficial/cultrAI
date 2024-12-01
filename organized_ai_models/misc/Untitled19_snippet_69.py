def update_endpoint_scaling(endpoint_name, min_replicas=1, max_replicas=2):
    endpoints = aiplatform.Endpoint.list(filter=f"display_name={endpoint_name}")
    if endpoints:
        endpoint = endpoints[0]
        endpoint.undeploy_all()
        endpoint.deploy(
            model=endpoint.model,
            deployed_model_display_name=endpoint_name,
            machine_type="n1-standard-2",
            min_replica_count=min_replicas,
            max_replica_count=max_replicas,
        )
        print(f"Updated scaling for endpoint: {endpoint_name}")
    else:
        print(f"Endpoint {endpoint_name} not found.")

update_endpoint_scaling("your_endpoint_name")
