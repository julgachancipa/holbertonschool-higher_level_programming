#!/usr/bin/python3
"""All cities by state"""
import sys
import MySQLdb
from sqlalchemy import create_engine

if __name__ == "__main__":

    mysql_usr = sys.argv[1]
    mysql_psw = sys.argv[2]
    db_name = sys.argv[3]
    state_nm = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_usr,
                           passwd=mysql_usr, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT
    cities.name
    FROM
    cities
    JOIN states ON states.id = cities.state_id
    WHERE
    states.name = %(state_nm)s
    ORDER BY cities.id ASC;
    """, {'state_nm': state_nm})

    query_rows = cur.fetchall()
    i = 0
    for row in query_rows:
        if i is not 0:
            print(' ,', end='')
        print(row[0], end='')
        i += 1
    print('')
    cur.close()
    conn.close()
