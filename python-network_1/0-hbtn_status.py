"""
This module fetches https://alu-intranet.hbtn.io/status and displays the body of the response.

Usage:
    python3 0-hbtn_status.py
"""

import requests


def main():
    """
    Sends a GET request to https://alu-intranet.hbtn.io/status and displays the body of the response.
    """
    url = "https://alu-intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))


if __name__ == "__main__":
    main()
