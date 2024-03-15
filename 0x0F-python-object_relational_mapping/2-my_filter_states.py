#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
accepts command line args:
                          -MySQl username
                          -MySQL user passwd
                          -Database name
                          -State name to be searched
"""

import MySQLdb
import sys


if __name__ == '__main__':
    argv = sys.argv
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    conn = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                           passwd=mysql_passwd, db=database_name)
    cur = conn.cursor()

    sql_query = ("SELECT * FROM states "
                 "WHERE states.name = '{}'"
                 .format(state_name_searched)
                 )

    cur.execute(sql_query)
    query_row = cur.fetchall()

    for row in query_row:
        print(row)

    cur.close()
    conn.close()
