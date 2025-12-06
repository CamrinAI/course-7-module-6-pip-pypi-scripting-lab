# lib/generate_log.py
from datetime import datetime

def generate_log(log_data):
    if not isinstance(log_data, list):
        raise ValueError("Input must be a list")

    filename = f"log_{datetime.now().strftime('%Y%m%d')}.txt"
    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")
    return filename

# Simple script entry point that demonstrates logging and API fetch

from lib.generate_log import generate_log
from datetime import datetime
import requests


def fetch_data():
    try:
        response = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
        if response.status_code == 200:
            return response.json()
    except requests.RequestException:
        pass
    return {}


if __name__ == "__main__":
    sample_log = ["User logged in", "User updated profile", "Report exported"]
    created = generate_log(sample_log)
    print(f"Log written to {created}")

    post = fetch_data()
    print("Fetched Post Title:", post.get("title", "No title found"))


