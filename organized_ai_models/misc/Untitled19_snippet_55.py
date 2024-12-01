def check_all_endpoints():
    print("Checking all endpoints...")
    endpoints = aiplatform.Endpoint.list()
    if not endpoints:
        print("No active endpoints found.")
    else:
        for endpoint in endpoints:
            print(f"Active Endpoint: {endpoint.display_name}, Resource Name: {endpoint.resource_name}")

check_all_endpoints()
