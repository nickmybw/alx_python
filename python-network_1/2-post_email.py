"""alX Task 2"""

import requests
import sys
"""
Sends a POST request to a URL with an email as a parameter and displays the body of the response
"""
if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)
