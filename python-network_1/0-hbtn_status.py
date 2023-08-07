"""
Module to fetch and display the status from a URL using requests.
"""

import requests


def fetch_status():
    """
    Fetches and displays the status from the specified URL.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    content = response.text

    print("Body response:")
    print("\t- type:", type(content))
    print("\t- content:", content)


if __name__ == "__main__":
    fetch_status()
