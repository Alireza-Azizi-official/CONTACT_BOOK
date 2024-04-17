from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QHBoxLayout,
    QMainWindow,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

class window(QMainWindow):
    def __init__(self,parent = None ) :
        super().__init__(parent)
        self.setWindowTitle("RP Contacts")
        self.resize(550,250)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.setupUI()
        
    def setupUI(self):
        self.table = QTableView
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        
        self.addButton = QPushButton("Add")
        self.deleteButton = QPushButton("Delete")
        self.clearbutton = QPushButton("Clear All")
        
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearbutton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)