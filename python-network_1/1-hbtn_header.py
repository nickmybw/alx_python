"""
Module to fetch and display the value of the X-Request-Id header from a URL using requests.
"""

import requests
import sys
"""
Sends a request to a URL and displays the value of the variable X-Request-Id in the response header
"""
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers.get('X-Request-Id'))
