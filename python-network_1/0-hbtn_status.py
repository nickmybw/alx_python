"""
This module fetches the status of two URLs and displays the body of the response.

Usage:
    python3 0-hbtn_status.py
"""

import requests


def main():
    """
    Sends GET requests to two URLs and displays the body of the response.
    """
    urls = ["https://intranet.hbtn.io/status", "http://0.0.0.0:5050/status"]
    for url in urls:
        response = requests.get(url)
        print("Body response:")
        print("\t- type: {}".format(type(response.text)))
        print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
