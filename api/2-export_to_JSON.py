"""the script will fetch data into a JSON file"""

import requests
import json
from sys import argv


def get_user_data(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        return None
    return user_response.json()


def get_todo_data(employee_id):
    todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todo_response = requests.get(todo_url)

    if todo_response.status_code != 200:
        return None
    return todo_response.json()


def export_to_json(employee_id, user_data, todo_data):
    if user_data is None:
        print("User not found")
        return
    if todo_data is None:
        print("TODO data not found")
        return

    user_id = user_data['id']
    username = user_data['username']

    json_data = {"USER_ID": []}
    for task in todo_data:
        task_title = task['title']
        task_completed = task['completed']
        json_data["USER_ID"].append(
            {"task": task_title, "completed": task_completed, "username": username})

    json_filename = f"{user_id}.json"

    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=4)

    print(f"Data exported to {json_filename}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 2-export_to_JSON.py <employee_id>")
    else:
        employee_id = int(argv[1])
        user_data = get_user_data(employee_id)
        todo_data = get_todo_data(employee_id)
        export_to_json(employee_id, user_data, todo_data)
