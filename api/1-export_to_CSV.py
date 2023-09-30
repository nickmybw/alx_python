"""
Gather data from an API and export to CSV
"""
import requests
import sys
import csv

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("Usage: ./1-export_to_CSV.py <employee_id>")

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

    employee_name = user_data.get("username")
    csv_filename = "{}.csv".format(employee_id)

    with open(csv_filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_data:
            task_id = task.get("id")
            task_title = task.get("title")
            task_completed = task.get("completed")
            csv_writer.writerow(
                [employee_id, employee_name, str(task_completed), task_title])

    print("Data exported to {}".format(csv_filename))
