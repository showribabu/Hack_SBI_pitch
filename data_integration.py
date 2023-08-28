import requests

def fetch_external_data(api_url):
    response = requests.get(api_url)
    data = response.json()
    return data

# Example usage
api_url = 'https://example.com/api/data'
external_data = fetch_external_data(api_url)
print(external_data)
