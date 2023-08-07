"""
This script sends a request to a specified URL and displays the value of the variable X-Request-Id in the response header.
"""

import requests
import sys


def get_request_id(url):
    """
    Sends a GET request to the specified URL and returns the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id header.
    """
    response = requests.get(url)
    return response.headers.get('X-Request-Id')


if __name__ == "__main__":
    url = sys.argv[1]
    request_id = get_request_id(url)
    print("X-Request-Id: {}".format(request_id))
