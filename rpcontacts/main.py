import sys
from PyQt5.QtWidgets import QApplication
from .views import window
from .database import createConnection
from PyQt5.QtSql import QSqlQuery


def main():
    app = QApplication(sys.argv)
    if not createConnection("contacts.sqlite"):
        sys.exit(app.exec())
    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
    """
    INSERT INTO contacts(
        name,
        job,
        email
    )
    VALUES(?, ?, ?)
    """
    )   
    
    data = [
        ("alireza","python programer", "aizizi@afdfd.com"),
        ("ghazal","java programer", "dfaf@afdfd.com"),
        ("reza","javascript programer", "afdfad@afdfd.com"),
        ("yeganeh","manager", "gdfgdfg@afdfd.com"),
        ("sara","project manager", "wrcvbgsd@afdfd.com"),
    ]
    
    for name, job, email in data:
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()
        
        
    win = window()
    win.show()
    sys.exit(app.exec_())
