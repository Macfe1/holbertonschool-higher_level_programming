#!/usr/bin/python3

import MySQLdb
import sys


def list_states(username, password, db_name):
    """
    Connects to the MySQL database and lists all states ordered by id.

    Args:
        username (str): The username for the database connection.
        password (str): The password for the database connection.
        db_name (str): The name of the database to connect to.

    Returns:
        None: Prints the states to the console.
    """

    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=db_name,
            port=3306
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_states(username, password, db_name)

    else:
        print("Usage: ./script.py username password db_name")
