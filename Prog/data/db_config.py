import pymysql

def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='root',
        password='9250',
        db='Друзья человека',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )