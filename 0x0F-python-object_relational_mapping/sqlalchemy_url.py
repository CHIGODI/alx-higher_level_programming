from sqlalchemy.engine.url import URL

mysql_db = {
    'drivername': 'mysql',
    'username': 'root',
    'password': '3778',
    'host': 'localhost',
    'port': 3306,
    'database': 'hbtn_0e_6_usa'  # Add the database parameter
}

print(URL(**mysql_db))
