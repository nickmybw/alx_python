import csv
import json
import sys

def export_to_csv(user_id):
    # Load data from your source (e.g., JSON data)
    with open('data.json', 'r') as data_file:
        data = json.load(data_file)

    # Filter tasks owned by the specified user
    user_tasks = [task for task in data if task['userId'] == user_id]

    # Define the CSV file name
    csv_filename = f"{user_id}.csv"

    # Write the tasks to the CSV file
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # Write the header row
        csv_writer.writerow(
            ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task as a row in the CSV file
        for task in user_tasks:
            csv_writer.writerow(
                [task['userId'], task['username'], str(task['completed']), task['title']])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    export_to_csv(user_id)
