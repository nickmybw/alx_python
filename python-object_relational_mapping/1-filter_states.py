"""aLX python object relational mapping task 1"""
import MySQLdb
import sys


def filter_states(username, password, database):
    """
    Lists all states from the database hbtn_0e_0_usa with a name starting with N (upper N).

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.

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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Fetch the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    # Call the filter_states function with the command line arguments
    filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
