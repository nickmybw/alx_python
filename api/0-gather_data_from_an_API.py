import requests
import sys


def get_employee_data(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com/"

    # Make a GET request to fetch employee details
    employee_response = requests.get(f"{base_url}users/{employee_id}")
    employee_data = employee_response.json()

    # Make a GET request to fetch employee's TODO list
    todo_response = requests.get(f"{base_url}users/{employee_id}/todos")
    todo_list = todo_response.json()

    return employee_data, todo_list


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])

    # Fetch employee data and TODO list
    employee_data, todo_list = get_employee_data(employee_id)

    # Extract relevant information
    employee_name = employee_data["name"]
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task["completed"])
    completed_task_titles = [task["title"]
                             for task in todo_list if task["completed"]]

    # Display the information in the specified format
    print(
        f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    for title in completed_task_titles:
        print(f"\t{title}")


if __name__ == "__main__":
    main()
