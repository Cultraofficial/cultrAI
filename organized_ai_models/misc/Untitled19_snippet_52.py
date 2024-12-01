def check_and_cleanup_endpoints():
    print("Checking active endpoints...")
    endpoints = aiplatform.Endpoint.list()
    for endpoint in endpoints:
        print(f"Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")
        if input(f"Undeploy all models from {endpoint.display_name}? (yes/no): ").lower() == "yes":
            endpoint.undeploy_all()
            print(f"Undeployed models from endpoint: {endpoint.display_name}")
        else:
            print(f"Skipping cleanup for: {endpoint.display_name}")

check_and_cleanup_endpoints()
