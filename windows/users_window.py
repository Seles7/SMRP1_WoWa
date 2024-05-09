from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_UsersWindow

from database import get_session, User


class Users(QMainWindow, Ui_UsersWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_goBack.clicked.connect(self.goBack())
        self.update_table()

    def update_table(self):
        users = self.session.query(User).order_by(User.id).all()
        self.tableWidget_Users.setRowCount(0)
        for user in users:
            row_position = self.tableWidget_Users.rowCount()
            self.tableWidget_Users.insertRow(row_position)
            self.tableWidget_Users.setItem(row_position, 0, QTableWidgetItem(str(user.id)))
            self.tableWidget_Users.setItem(row_position, 1, QTableWidgetItem(user.username))

    def showWindow(self):
        self.show()

    def goBack(self):
        self.close()