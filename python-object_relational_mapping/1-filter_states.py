#!/usr/bin/python3
"""
This script connects to a MySQL database using credentials.
It retrieves and displays all states from the 'states' table
where the name starts with 'N',ordered by their 'id'
in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function:

    Retrieves MySQL credentials and the database name
    from command-line arguments.
    Connects to the specified MySQL database on
    localhost at port 3306, executes a query to select
    all states whose names start with 'N', ordered
    by 'id' in ascending order, and prints each result.
    """

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name,
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE BINARY "
                   "name LIKE 'N%' ORDER BY id ASC ")

    states_n = cursor.fetchall()

    for iter_state in states_n:
        print(iter_state)

    cursor.close()
    db.close()
