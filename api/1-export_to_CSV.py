"""
Export to CSV
"""
import csv
import requests
from sys import argv


if __name__ == '__main__':
    user_id = argv[1]
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    todo_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
        user_id)

    user_response = requests.get(user_url)
    todo_response = requests.get(todo_url)

    user_data = user_response.json()
    todo_data = todo_response.json()

    employee_name = user_data.get('username')
    file_name = '{}.csv'.format(user_id)

    with open(file_name, mode='w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_ALL)

        for task in todo_data:
            task_completed = task.get('completed')
            task_title = task.get('title')
            writer.writerow(
                [user_id, employee_name, task_completed, task_title])
