import requests
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        return

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        # Fetch employee details
        employee_response = requests.get(f"{base_url}/users/{employee_id}")
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch employee's TODO list
        todos_response = requests.get(f"{base_url}/users/{employee_id}/todos")
        todos_data = todos_response.json()

        # Calculate completed and total tasks
        total_tasks = len(todos_data)
        completed_tasks = sum(
            1 for task in todos_data if task.get("completed"))

        # Display the result
        print(
            f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
        for task in todos_data:
            if task.get("completed"):
                print(f"\t{task.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return


if __name__ == "__main__":
    main()
