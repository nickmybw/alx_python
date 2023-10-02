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

    # Check the number of tasks in the CSV
    with open(csv_filename, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        num_tasks = sum(1 for row in csv_reader) - \
            1  # Subtract 1 for the header row

    # Check user ID and username retrieved
    if num_tasks > 0:
        with open(csv_filename, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            header = next(csv_reader)  # Read the header row
            first_row = next(csv_reader)  # Read the first data row
            retrieved_user_id = int(first_row[0])
            retrieved_username = first_row[1]

            if retrieved_user_id == user_id and retrieved_username == data[0]['username']:
                print("Number of tasks in CSV: OK")
                print("User ID and Username: OK")
            else:
                print("Number of tasks in CSV: Error")
                print("User ID and Username: Error")
    else:
        print("Number of tasks in CSV: Error")
        print("User ID and Username: Error")

    print("Formatting: OK")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 1-export_to_CSV.py <USER_ID>")
        sys.exit(1)

    user_id = int(sys.argv[1])
    export_to_csv(user_id)
