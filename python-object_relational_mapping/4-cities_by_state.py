"""
Module documentation: This script connects to a MySQL database and retrieves
cities along with their corresponding state names from the 'cities' and 'states' tables.
"""

import sys
import MySQLdb


def list_cities_by_state(username, password, db_name):
    """
    Function documentation: Connects to the database and retrieves values
    from the 'states' table based on the provided state name in a safe way.
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
        db = MySQLdb.connect(
            host="localhost", port=3306, user=username,
            passwd=password, db=db_name
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Execute the SQL query to retrieve cities with their state names
        query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            INNER JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
        """
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

    list_cities_by_state(username, password, db_name)
