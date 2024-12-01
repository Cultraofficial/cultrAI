import requests

backend_url = "https://backend-f15f29b1-336c-4159-b89f-50a835eafa6e.nhost.run/v1/graphql"

try:
    response = requests.head(backend_url)
    if response.status_code == 200:
        print("Nhost backend is reachable.")
    else:
        print(f"Nhost backend returned status code: {response.status_code}")
except requests.ConnectionError as e:
    print("Failed to connect to the Nhost backend:", e)
