import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='user',
        password='password',
        db='animals_db',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )