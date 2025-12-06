import requests

DEFAULT_URL = "https://jsonplaceholder.typicode.com/posts/1"


def fetch_data(url: str = DEFAULT_URL) -> dict:
    """Fetch JSON data from the given URL.

    Returns an empty dict on non-200 response or exceptions.
    """
    try:
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            return resp.json()
    except requests.RequestException:
        pass
    return {}
