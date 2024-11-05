#!/usr/bin/python3
"""
This script connects to a MySQL database and retrieves all states
from the 'states' table, displaying them in ascending order by id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    The main function of the script. It retrieves MySQL credentials
    from command line arguments, connects to the specified database,
    executes a query to retrieve all states, and prints them.
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

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for iter_state in states:
        print(iter_state)

    cursor.close()
    db.close()
