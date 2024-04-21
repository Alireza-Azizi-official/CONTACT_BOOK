import sys
from PyQt5.QtWidgets import QApplication
from .views import Window
from .database import createConnection
from PyQt5.QtSql import QSqlQuery

def main():
    app = QApplication(sys.argv)
    if not createConnection("contacts.sqlie"):
        sys.exit(1)
    
    insertDataQuery = QSqlQuery()
    insertDataQuery.prepare(
    """
    INSERT INTO contacts(
        name,
        job,
        email
    )
    VALUES (?, ?, ?)
    """
    )
    data =[
        ("hassan", "english teacher", "hassan@example.com"),
        ("reza", "math teacher", "reza@example.com"),
        ("masoud", "physic teacher", "masoud@example.com"),
        ("alireza", "art teacher", "alireza@example.com"),
        ("karim", "Sport teacher", "karim@example.com"),
    ]
    
    for name, job, email in data :
        insertDataQuery.addBindValue(name)
        insertDataQuery.addBindValue(job)
        insertDataQuery.addBindValue(email)
        insertDataQuery.exec()

    win = Window(None)
    win.show()
    sys.exit(app.exec())