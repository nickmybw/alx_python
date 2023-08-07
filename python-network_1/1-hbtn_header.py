"""
Module to fetch and display the value of the X-Request-Id header from a URL using requests.
"""

import requests
import sys


def fetch_x_request_id(url):
    """
    Fetches and displays the value of the X-Request-Id header from the response.
    """
    response = requests.get(url)
    x_request_id = response.headers.get('X-Request-Id')

    if x_request_id:
        print(x_request_id)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    fetch_x_request_id(url)
