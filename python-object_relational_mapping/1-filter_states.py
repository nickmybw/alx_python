"""
Module documentation: This script connects to a MySQL database and retrieves
states whose names start with 'N' from the 'states' table in ascending order
based on 'id'.
"""

import sys
import MySQLdb


def filter_states(username, password, db_name):
    """
    Function documentation: Connects to the MySQL database and retrieves states
    whose names start with 'N' from the 'states' table in ascending order based
    on 'id'.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.

    Returns:
        None.
    """
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to filter states starting with 'N'
        query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all rows and display them
        results = cursor.fetchall()
        for row in results:
            print(row)

    except MySQLdb.Error as e:
        print("MySQL Error: {}".format(e))
    finally:
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    filter_states(username, password, db_name)
