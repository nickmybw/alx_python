"""ALX Python Network Task 4"""

import requests
import sys
"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter and displays the response
"""

if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {'q': letter}
    response = requests.post(url, data=data)

    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get(
                'id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
