import sys
import requests


def get_employee_details(employee_id):
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}')
    return response.json()


def get_employee_todos(employee_id):
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos')
    return response.json()


def display_employee_todo_progress(employee_id):
    employee_details = get_employee_details(employee_id)
    employee_todos = get_employee_todos(employee_id)

    done_tasks = 0
    for todo in employee_todos:
        if todo['completed']:
            done_tasks += 1

    print(
        f"Employee {employee_details['name']} is done with tasks({done_tasks}/{len(employee_todos)}):")

    for todo in employee_todos:
        if todo['completed']:
            print(f"\t{todo['title']}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    display_employee_todo_progress(employee_id)
