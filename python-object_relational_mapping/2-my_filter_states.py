"""aLX python object relational mapping task 2"""
import MySQLdb
import sys


def filter_states_by_user_input(username, password, database, state_name):
    """
    Lists all states from the database hbtn_0e_0_usa where name matches the argument.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        database (str): The name of the database.
        state_name (str): The name of the state to search for.

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
    query = "SELECT * FROM states WHERE name LIKE '{}' ORDER BY id ASC".format(
        state_name)
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Display the results
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == '__main__':
    # Call the filter_states_by_user_input function with the command line arguments
    filter_states_by_user_input(
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
