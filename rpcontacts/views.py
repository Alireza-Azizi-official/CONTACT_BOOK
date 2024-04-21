from .model import ContactsModel
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
    QAbstractItemView,
    QDialog,
    QDialogButtonBox,
    QFormLayout,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QTableView,
    QVBoxLayout,
    QWidget,
)

class Window (QMainWindow):
    def __init__(self, parent: None) :
        super().__init__(parent)
        self.setWindowTitle("CONTACT BOOK")
        self.resize(870,600)
        self.centralWidget =QWidget()
        self.setCentralWidget(self.centralWidget)
        self.layout = QHBoxLayout()
        self.centralWidget.setLayout(self.layout)
        self.contactsModel = ContactsModel()
        self.setupUI()
        
        
    def setupUI(self):
        self.table = QTableView()
        self.table.setModel(self.contactsModel.model)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.resizeColumnsToContents()
        self.addButton = QPushButton("Add")
        self.addButton.clicked.connect(self.openAddDialog)
        self.deleteButton = QPushButton("Delete")
        self.deleteButton.clicked.connect(self.deleteContact)
        self.clearAllButton = QPushButton("Clear All")
        self.clearAllButton.clicked.connect(self.clearContacts)
        layout = QVBoxLayout()
        layout.addWidget(self.addButton)
        layout.addWidget(self.deleteButton)
        layout.addStretch()
        layout.addWidget(self.clearAllButton)
        self.layout.addWidget(self.table)
        self.layout.addLayout(layout)
        
    def openAddDialog(self):
        dialog = AddDialog(self)
        if dialog.exec() == QDialog.Accepted:
            self.contactsModel.addContact(dialog.data)
            self.table.resizeColumnsToContents()
        
    def deleteContact(self):
        row = self.table.currentIndex().row()
        if row < 0:
            return
        messageBox = QMessageBox.warning(
            self,
            "Warning!",
            "Do you want to remove the selected contact?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )

        if messageBox == QMessageBox.Ok:
            self.contactsModel.deleteContact(row)
            
    def  clearContacts(self):
        messageBox = QMessageBox.warning(
            self,
            "WARNING",
            "Do you want to remove all your contacts?",
            QMessageBox.Ok | QMessageBox.Cancel,
        )
        if messageBox == QMessageBox.Ok:
            self.contactsModel.clearContacts()
            
            
class AddDialog(QDialog):
    def __init__(self, parent: None):
        super().__init__(parent=parent)
        self.setWindowTitle("Add contactt")
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        self.data = None
        self.setupUI()
        
    def setupUI(self):
        self.nameField = QLineEdit()
        self.nameField.setObjectName("Name")
        self.jobField = QLineEdit()
        self.jobField.setObjectName("Job")
        self.emaiField = QLineEdit()
        self.emaiField.setObjectName("Email")
        
        layout = QFormLayout()
        layout.addRow("Name", self.nameField)
        layout.addRow("Job", self.jobField)
        layout.addRow("Email", self.emaiField)
        self.layout.addLayout(layout)
        
        self.buttonBox = QDialogButtonBox(self)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        self.layout.addWidget(self.buttonBox)
        
    def accept(self):
        self.data = []
        for field in (self.nameField, self.jobField, self.emaiField):
            if not field.text():
                QMessageBox.critical(
                    self,
                    "Error",
                    f"you must provide a contact's {field.objectName()}",
                )
                self.data = None 
                return
            self.data.append(field.text())
        super().accept()