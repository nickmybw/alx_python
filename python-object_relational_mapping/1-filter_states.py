"""aLX python object relational mapping task 1"""
import MySQLdb


def filter_states(username, password, database):
    """
    Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database (str): Database name.

    Returns:
        None
    """
    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)

    # Create a cursor object
    cursor = db.cursor()

    # Execute the SQL query
    query = "SELECT * FROM hbtn_0e_0_usa WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and display the results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    filter_states("your_username", "your_password", "your_database")
