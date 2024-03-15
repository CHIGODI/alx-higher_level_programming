#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa sorted by id
accepts command line args:
                          -MySQl username
                          -MySQL user passwd
                          -Database name
"""
import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    database_name = argv[3]

    conn = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                           passwd=mysql_passwd, db=database_name)
    cur = conn.cursor()

    cur.execute('SELECT * FROM  states ORDER BY states.id')
    query_columns = cur.fetchall()

    for row in query_columns:
        print(row)

    cur.close()
    conn.close()
