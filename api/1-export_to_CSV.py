import csv
import requests
import sys
import cvs


def fetch_employee_data(employee_id):
    # Define the API endpoints for the employee and their TODO list
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch data from the API
    employee_response = requests.get(employee_url)
    todo_response = requests.get(todo_url)

    # Check if the requests were successful
    if employee_response.status_code != 200:
        print("Error: Unable to fetch employee data.")
        sys.exit(1)
    if todo_response.status_code != 200:
        print("Error: Unable to fetch TODO list data.")
        sys.exit(1)

    # Parse JSON responses
    employee_data = employee_response.json()
    todo_list = todo_response.json()

    return employee_data, todo_list


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    employee_data, todo_list = fetch_employee_data(employee_id)

    employee_name = employee_data.get('name')
    completed_tasks = [task for task in todo_list if task['completed']]
    total_tasks = len(todo_list)

    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")

    for task in completed_tasks:
        print(f"\t{task['title']}")


def export_to_csv(employee_id, employee_name, todo_list):
    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            csv_writer.writerow(
                [employee_id, employee_name, task['completed'], task['title']])

    print(f"Data has been exported to {csv_file_name}")


def main():
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python3 1-export_to_CSV.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    employee_data, todo_list = fetch_employee_data(employee_id)

    employee_name = employee_data.get('name')
    completed_tasks = [task for task in todo_list if task['completed']]

    print(
        f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{len(todo_list)}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

    export_to_csv(employee_id, employee_name, todo_list)


if __name__ == "__main__":
    main()
