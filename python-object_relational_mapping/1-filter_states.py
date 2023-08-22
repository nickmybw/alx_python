"""
Lists all states with a name starting with N (upper N) from the database test_1
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connects to MySQL server running on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db="test_1")
    # Executes the SQL query
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    # Prints the results
    for row in cur.fetchall():
        print(row)
    # Closes all cursors and the database connection
    cur.close()
    db.close()
