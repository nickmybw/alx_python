"""aLX python object relational mapping task 5"""

import MySQLdb
import sys


def list_cities(username, password, database, state_name):
    """
    Lists all cities of a state from the database hbtn_0e_4_usa.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.
        state_name (str): The name of the state.

    Returns:
        None

    Raises:
        MySQLdb.Error: If there is an error executing the query.

    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query
    query = ["SELECT cities.name FROM cities",
    "JOIN states ON cities.state_id = states.id",
    "WHERE states.name = %s",
    "ORDER BY cities.id ASC"]
    query = " ".join(query)
    cursor.execute(query, (state_name,))

    # Fetch the results
    results = cursor.fetchall()

    # Display the results
    cities = [row[0] for row in results]
    print(", ".join(cities))

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    # Call the list_cities function with the command line arguments
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
