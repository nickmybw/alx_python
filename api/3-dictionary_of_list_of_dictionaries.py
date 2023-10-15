import requests
import json

def export_all_employees_todo():
    # Define the API endpoint for all users
    users_url = 'https://jsonplaceholder.typicode.com/users'

    # Fetch user information for all employees
    users_response = requests.get(users_url)
    if users_response.status_code != 200:
        print("Failed to fetch user data.")
        return

    users_data = users_response.json()
    
    all_employees_data = {}

    for user in users_data:
        user_id = user['id']
        username = user['name']
        user_todos_url = f'https://jsonplaceholder.typicode.com/users/{user_id}/todos'

        # Fetch the TODO list for the employee
        todos_response = requests.get(user_todos_url)
        if todos_response.status_code == 200:
            todos_data = todos_response.json()
            user_tasks = []

            for todo in todos_data:
                user_task = {
                    "username": username,
                    "task": todo['title'],
                    "completed": todo['completed']
                }
                user_tasks.append(user_task)

            all_employees_data[user_id] = user_tasks

    # Export data to a JSON file
    json_filename = 'todo_all_employees.json'
    with open(json_filename, 'w') as json_file:
        json.dump(all_employees_data, json_file, indent=4)

if __name__ == "__main__":
    export_all_employees_todo()
