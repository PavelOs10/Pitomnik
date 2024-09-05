from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def get_db_connection():
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('animals.sqlite')
    if not db.open():
       print("Cannot establish a database connection")
    return db

def create_tables():
    query = QSqlQuery()
    query.exec_("""
    CREATE TABLE IF NOT EXISTS Все_животные (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        имя TEXT,
        тип TEXT,
        команды TEXT
    )
    """)