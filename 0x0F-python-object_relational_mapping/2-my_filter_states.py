#!/usr/bin/python3
"""Filter states by user input"""
import sys
import MySQLdb
from sqlalchemy import create_engine

if __name__ == "__main__":

    mysql_usr = sys.argv[1]
    mysql_psw = sys.argv[2]
    db_name = sys.argv[3]
    str_search = sys.argv[4]

    conn = MySQLdb.connect(host="localhost", port=3306, user=mysql_usr,
                           passwd=mysql_usr, db=db_name, charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
                .format(str_search))
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == str_search:
            print(row)
    cur.close()
    conn.close()
