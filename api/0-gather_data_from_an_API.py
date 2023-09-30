"""
Gather data from an API
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./0-gather_data_from_an_API.py <employee_id>")

    employee_id = sys.argv[1]

    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(
        employee_id)
    todo_url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
        employee_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    if user_response.status_code != 200:
        sys.exit("Error: User data not found")

    if todo_response.status_code != 200:
        sys.exit("Error: TODO data not found")

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get("name")
    total_tasks = len(todo_data)
    completed_tasks = [task for task in todo_data if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(completed_tasks), total_tasks))

    for task in completed_tasks:
        print("\t {}".format(task.get("title")))
