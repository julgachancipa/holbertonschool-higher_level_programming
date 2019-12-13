#!/usr/bin/python3
"""Filter states states"""
import sys
import MySQLdb
from sqlalchemy import create_engine

if __name__ == "__main__":

    mysql_usr = sys.argv[1]
    mysql_psw = sys.argv[2]
    db_name = sys.argv[3]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_usr,
                           passwd=mysql_usr, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name REGEXP '^[N]' ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
