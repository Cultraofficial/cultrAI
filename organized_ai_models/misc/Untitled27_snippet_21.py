def fetch_and_store_multiple(api_urls, firebase_config):
    """
    Fetch data from multiple APIs and store it in Firebase.

    :param api_urls: List of API endpoints to fetch data from.
    :param firebase_config: Firebase configuration dictionary.
    """
    try:
        # Initialize Firebase
        firebase = pyrebase.initialize_app(firebase_config)
        db = firebase.database()

        for idx, api_url in enumerate(api_urls):
            print(f"Fetching data from API {idx + 1}: {api_url}...")
            response = requests.get(api_url)

            if response.status_code != 200:
                print(f"Error: Failed to fetch data from {api_url}. Status code: {response.status_code}")
                continue

            data = response.json()  # Parse JSON response

            # Store data in Firebase under a unique node
            node_name = f"api_data_{idx + 1}"
            print(f"Storing data in Firebase under node '{node_name}'...")
            db.child(node_name).set(data)
            print(f"Data successfully stored in Firebase under node '{node_name}'!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
api_urls = [
    "https://jsonplaceholder.typicode.com/todos/1",
    "https://jsonplaceholder.typicode.com/todos/2"
]
fetch_and_store_multiple(api_urls, firebase_config)
