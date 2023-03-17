#!/usr/bin/python3
"""
list all cities from db
"""
from sys import argv
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3],
                         port=3306)

    cur = db.cursor()
    stmt = """
    SELECT cities.id, cities.name, states.name
    FROM cities JOIN states
    WHERE cities.state_id=states.id;
    """
    cur.execute(stmt)

    cities = cur.fetchall()

    for city in cities:
        print(city)
