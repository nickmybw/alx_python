import csv

# open the file in the write mode
with open('USER_ID.csv', 'w', newline='') as f:
    # create the csv writer
    writer = csv.writer(f)

    # write the header row
    writer.writerow(
        ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

    # write the data rows
    for task in tasks:
        writer.writerow([task.user_id, task.username,
                        task.completed_status, task.title])
