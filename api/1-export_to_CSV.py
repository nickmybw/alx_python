"""
Export data to CSV
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

    employee_id = user_data.get("id")
    employee_name = user_data.get("username")

    completed_tasks = [(employee_id, employee_name, task.get(
        "completed"), task.get("title")) for task in todo_data]

    csv_file = "{}.csv".format(employee_id)

    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(completed_tasks)

    print("Data exported to {}.csv".format(employee_id))
