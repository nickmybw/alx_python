"""ALX Python-Network Task 3"""

import requests
import sys
"""
Sends a request to a URL and displays the body of the response
"""
if __name__ == "__main__":
    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
