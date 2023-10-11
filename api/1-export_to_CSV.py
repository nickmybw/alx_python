import requests
import csv
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


def export_to_csv(employee_id, user_data, todo_data):
    if user_data is None:
        print("User not found")
        return
    if todo_data is None:
        print("TODO data not found")
        return

    user_id = user_data['id']
    username = user_data['username']
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_data:
            task_id = task['id']
            task_title = task['title']
            task_completed = task['completed']
            csv_writer.writerow(
                [user_id, username, task_completed, task_title])
        print(f"Data exported to {csv_filename}")


if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        user_data = get_user_data(employee_id)
        todo_data = get_todo_data(employee_id)
        export_to_csv(employee_id, user_data, todo_data)
