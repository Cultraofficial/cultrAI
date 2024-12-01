def cleanup_all_endpoints():
    print("Checking and cleaning up all Vertex AI endpoints...")
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Undeploying models from endpoint: {endpoint.display_name}")
        endpoint.undeploy_all()
        print(f"Deleting endpoint: {endpoint.display_name}")
        endpoint.delete()

cleanup_all_endpoints()
