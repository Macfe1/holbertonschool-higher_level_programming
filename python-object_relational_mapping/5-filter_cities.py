#!/usr/bin/python3
"""
This script connects to a MySQL database using provided credentials
and retrieves all cities from the 'cities' table in the specified
database where the state name matches the provided argument.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    """
    Main function that retrieves MySQL credentials, database name,
    and state name from command-line arguments. It connects to the
    MySQL database on localhost, executes a query to select cities
    associated with the provided state name, and prints the results.
    """

    if len(sys.argv) != 5:
        print("Must be 5 arguments")
        sys.exit(1)

    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )

    cursor = db.cursor()

    query = """
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            """

    cursor.execute(query, (state_name,))

    cities = cursor.fetchall()

    print(", ".join(city[0] for city in cities))

    cursor.close()
    db.close()
