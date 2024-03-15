#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
accepts command line args:
                          -MySQl username
                          -MySQL user passwd
                          -Database name
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    argv = sys.argv
    mysql_username = argv[1]
    mysql_passwd = argv[2]
    database_name = argv[3]
    state_name = argv[4]

    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=mysql_username,
                           passwd=mysql_passwd,
                           db=database_name)
    cur = conn.cursor()

    sql_query = ('SELECT cities.name '
                 'FROM cities '
                 'LEFT JOIN states '
                 'ON states.id = cities.state_id '
                 'WHERE states.name = %s '
                 'ORDER BY cities.id ASC')
    cur.execute(sql_query, (state_name,))
    query_rows = cur.fetchall()

    for index, row in enumerate(query_rows):
        for city in row:
            if index < len(query_rows) - 1:
                print(city, end=', ')
            else:
                print(city)

    cur.close()
    conn.close()
