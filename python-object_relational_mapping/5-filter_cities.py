"""aLX python object relational mapping task 5"""

import sys
import MySQLdb


def filter_cities_by_state(username, password, db_name, state_name):
    """
    Function documentation: Connects to the MySQL database and retrieves cities
    of a specified state from the 'cities' and 'states' tables.

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

        # Create the SQL query with user input and execute
        query = (
            "SELECT GROUP_CONCAT(cities.name ORDER BY cities.id ASC SEPARATOR ', ') "
            "FROM cities "
            "INNER JOIN states ON cities.state_id = states.id "
            "WHERE states.name = %s"
        )
        cursor.execute(query, (state_name,))

        # Fetch the result and display it
        result = cursor.fetchone()
        if result:
            print(result[0])

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

    filter_cities_by_state(username, password, db_name, state_name)
