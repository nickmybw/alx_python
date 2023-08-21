"""aLX python object relational mapping task 1"""
import MySQLdb
import sys


def filter_states(username, password, db_name):
    """
    Lists all states with a name starting with N (upper N) from the database hbtn_0e_0_usa.

    Args:
        username (str): The MySQL username.
        password (str): The MySQL password.
        db_name (str): The name of the database.

    Returns:
        None
    """
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    data = cursor.fetchall()
    for row in data:
        print(row)
    cursor.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    filter_states(username, password, db_name)
