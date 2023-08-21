"""aLX python object relational mapping task 2
Module documentation: This script connects to a MySQL database and retrieves
values from the 'states' table based on the provided state name.
"""

import sys
import MySQLdb
def filter_states_by_name(username, password, db_name, state_name):
    """
    Function documentation: Connects to the MySQL database and retrieves values
    from the 'states' table based on the provided state name.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        db_name (str): Database name.
        state_name (str): State name to search for.

    Returns:
        None.
    """
    try:
        # Connect to the database
        db = MySQLdb.connect(host="localhost", port=3306, user=username,
                             passwd=password, db=db_name)

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Create the SQL query with user input and execute it
        query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

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
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    filter_states_by_name(username, password, db_name, state_name)
