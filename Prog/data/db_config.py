from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def get_db_connection():
    db = QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setDatabaseName('Друзья человека')
    db.setUserName('root')
    db.setPassword('9250')
    if not db.open():
        print("Cannot establish a database connection")
    return db