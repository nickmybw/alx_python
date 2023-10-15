import requests
import sys
import json

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch user information
    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        print(f"Employee with ID {employee_id} not found.")
        return

    user_data = user_response.json()
    user_id = user_data['id']
    employee_name = user_data['name']

    # Fetch the TODO list for the employee
    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        print(f"TODO list for employee with ID {employee_id} not found.")
        return

    todos_data = todos_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Display the progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

    # Display the titles of completed tasks
    for todo in todos_data:
        if todo['completed']:
            print(f"\t{todo['title']}")

    # Export data to JSON
    json_filename = f'{user_id}.json'
    export_data = {
        "USER_ID": [
            {
                "task": todo['title'],
                "completed": todo['completed'],
                "username": employee_name
            }
            for todo in todos_data
        ]
    }

    with open(json_filename, 'w') as json_file:
        json.dump(export_data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
