query = {
    "query": """
    query {
        launchesPast(limit: 1) {
            mission_name
            launch_date_utc
        }
    }
    """
}

response = requests.post("https://api.spacex.land/graphql/", json=query)
print(response.json())
