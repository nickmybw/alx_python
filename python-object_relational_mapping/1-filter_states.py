"""
Script that lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Check if all arguments are provided
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    # Create a cursor to interact with the database
    cur = db.cursor()

    # Execute the query to select states starting with 'N' (upper N)
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cur.execute(query)

    # Fetch and display the results
    results = cur.fetchall()
    for row in results:
        print(row)

    # Close cursor and connection
    cur.close()
    db.close()
