import requests
from sys import argv
import csv  # Import the csv module
from typing import List, Any

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
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

            completed_tasks: List[Any] = [
                task for task in todo_data if task['completed']]
            total_tasks = len(todo_data)

            print(
                f"Employee {user_data['name']} is done with tasks({len(completed_tasks)}/{total_tasks}):")
            for task in completed_tasks:
                print(f"\t {task['title']}")

            # Export data to CSV
            csv_file_name = f"{employee_id}.csv"
            with open(csv_file_name, mode='w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(
                    ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

                for task in todo_data:
                    csv_writer.writerow(
                        [user_data['id'], user_data['username'], task['completed'], task['title']])

            print(f"Data exported to {csv_file_name}")
