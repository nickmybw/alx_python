"""
Module to fetch and display the status from a URL using requests.
"""

import requests
"""
Fetches https://alu-intranet.hbtn.io/status using requests package
"""

if __name__ == "__main__":
    url = 'https://alu-intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
