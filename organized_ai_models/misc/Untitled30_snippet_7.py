import requests

try:
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    if response.status_code == 200:
        print("API request successful:")
        print(response.json()[0])  # Print the first post
    else:
        print("API request failed.")
except requests.ConnectionError:
    print("Unable to connect to the API.")
