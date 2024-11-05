#!/usr/bin/python3
"""
This script connects to a MySQL database using given credentials
and retrieves all states from the 'states' table in the specified
database where the state name matches the provided argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that retrieves MySQL credentials, database name,
    and state name from command-line arguments. It connects to the
    MySQL database on localhost, executes a query to select states
    matching the provided name,and prints the results
    ordered by 'id' in ascending order.
    """

    if len(sys.argv) != 4:
        print("Must be 4 arguments")
        sys.exit(1)

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )

    cursor = db.cursor()

    query = """
            SELECT cities.id, cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id ASC
            """

    cursor.execute(query)

    cities = cursor.fetchall()

    for iter_city in cities:
        print(iter_city)

    cursor.close()
    db.close()
