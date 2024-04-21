import sys
from PyQt5.QtWidgets import QApplication
from .views import Window
from .database import createConnection


def main():
    app = QApplication(sys.argv)
    if not createConnection("contacts.sqlie"):
        sys.exit(1)
    win = Window(None)
    win.show()
    sys.exit(app.exec())