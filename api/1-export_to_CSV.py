"""
Gather data from an API
"""
import requests
import sys
import csv


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
