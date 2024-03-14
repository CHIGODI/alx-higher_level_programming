#!/usr/bin/python3
"""
script that lists all states with a name starting with N (upper N)
from the database hbtn_0e_0_usa
accepts command line args:
                          -MySQl username
                          -MySQL user passwd
                          -Database name
"""
import MySQLdb
import sys

argv = sys.argv
mysql_username = argv[1]
mysql_passwd = argv[2]
database_name = argv[3]
state_name_searched = argv[4]

conn = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                       passwd=mysql_passwd, db=database_name)
cur = conn.cursor()

sql_query = 'SELECT * FROM states WHERE name = %s ORDER BY id ASC'

cur.execute(sql_query, (state_name_searched,))
query_row = cur.fetchall()

for row in query_row:
    print(row)

cur.close()
conn.close()

if __name__ == '__main__':
    pass
