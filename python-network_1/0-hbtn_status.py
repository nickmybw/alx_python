"""
This module fetches the status of a specified URL using the requests module.

Usage:
    python3 0-hbtn_status.py
"""

import requests


def fetch_status(url):
    """
    Sends a GET request to the specified URL and displays the body of the response.

    Args:
        url (str): The URL to fetch the status from.

    Returns:
        str: The body of the response.
    """
    response = requests.get(url)
    return response.text


def main():
    """
    Main function that fetches the status of two URLs and displays the output.
    """
    url1 = "https://intranet.hbtn.io/status"
    url2 = "http://0.0.0.0:5050/status"
    print("Body response:")
    print("\t- type: {}".format(type(fetch_status(url1))))
    print("\t- content: {}".format(fetch_status(url1)))
    print("Body response:")
    print("\t- type: {}".format(type(fetch_status(url2))))
    print("\t- content: {}".format(fetch_status(url2)))


if __name__ == "__main__":
    main()
