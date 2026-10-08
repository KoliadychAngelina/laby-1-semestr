import requests

def fetch_http_status(url: str = "https://httpbin.org/get") -> int:
    response = requests.get(url)
    return response.status_code