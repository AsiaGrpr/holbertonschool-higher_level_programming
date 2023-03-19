#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb
import sys


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("""
        SELECT cities.name
        FROM cities
        LEFT JOIN states
        ON states.id = cities.state_id
        WHERE states.name = %s ORDER BY cities.id ASC
        """, (sys.argv[4],))

    resultfetch = cursor.fetchall()

    cities = ""
    sep = ""
    for i in resultfetch:
        cities += sep + i[0]
        sep = ", "
    print(cities)

    cursor.close()
    db.close()
