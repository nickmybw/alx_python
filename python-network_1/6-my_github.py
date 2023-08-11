"""ALX Python Network Task 5"""

import requests
import sys
"""
Uses the GitHub API to display your id
"""
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, password))

    try:
        json_response = response.json()
        print(json_response.get('id'))
    except ValueError:
        print("Not a valid JSON")
