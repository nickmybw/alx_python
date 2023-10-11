import requests
import csv
from sys import argv

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
    else:
        employee_id = int(argv[1])
        user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
        todo_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

        user_response = requests.get(user_url)
        todo_response = requests.get(todo_url)

        if user_response.status_code != 200:
            print("User not found")
        elif todo_response.status_code != 200:
            print("TODO data not found")
        else:
            user_data = user_response.json()
            todo_data = todo_response.json()
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
