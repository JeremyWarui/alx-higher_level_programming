#!/usr/bin/python3
"""
takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
safe from MySQL injections
"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(port=3306,
                         host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
    SELECT * FROM states
    WHERE name='%s'
    """, sys.argv[4])
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()
