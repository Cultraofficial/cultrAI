import requests

def download_file_from_google_drive(file_id, destination):
    URL = "https://drive.google.com/uc?export=download"

    with requests.Session() as session:
        response = session.get(URL, params={'id': file_id}, stream=True)
        token = get_confirm_token(response)

        if token:
            params = {'id': file_id, 'confirm': token}
            response = session.get(URL, params=params, stream=True)

        save_response_content(response, destination)

def get_confirm_token(response):
    for key, value in response.cookies.items():
        if key.startswith('download_warning'):
            return value
    return None

def save_response_content(response, destination):
    CHUNK_SIZE = 32768

    with open(destination, "wb") as f:
        for chunk in response.iter_content(CHUNK_SIZE):
            if chunk:
                f.write(chunk)

# Example usage
file_id = 'your_file_id_here'  # Extract file id from sharable link
destination = 'path_to_save_model'
download_file_from_google_drive(file_id, destination)