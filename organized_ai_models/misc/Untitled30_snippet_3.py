query = {
    "query": """
    query {
        users {
            id
            email
        }
    }
    """
}

response = requests.post(backend_url, json=query, headers=headers)
print(response.json())  # Check the response
