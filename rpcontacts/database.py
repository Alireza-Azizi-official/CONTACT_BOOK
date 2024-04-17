from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

def _createconnectiontable():
    createtablequery = QSqlQuery()
    return createtablequery.exec(
        """
        CREATE TABLE IF NOT EXISTS  contact (
            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE NOT NULL,
            name VARCHAR(40) NOT NULL,
            job VARCHAR(50),
            email VARCHAR(40) NOT NULL
        )
        """
    )

def createconnection(databasename):
    connection = QSqlDatabase.addDatabase("QSQLITE")
    connection.setDatabaseName(databasename)
    
    if not connection.open():
        QMessageBox.warning(
            None,
            "RP Contact",
            f"Database error: {connection.lastError().text}",
        )
        return False
    _createconnectiontable()
    return True