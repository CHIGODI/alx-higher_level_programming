#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
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

conn = MySQLdb.connect(host='localhost', port=3306, user=mysql_username,
                       passwd=mysql_passwd, db=database_name)
cur = conn.cursor()

sql_query = ('SELECT cities.id, cities.name, states.name '
             'FROM cities '
             'LEFT JOIN states '
             'ON states.id = cities.state_id '
             'ORDER BY cities.id ASC')
cur.execute(sql_query)
query_rows = cur.fetchall()

for row in query_rows:
    print(row)

cur.close()
conn.close()

if __name__ == '__main__':
    pass
