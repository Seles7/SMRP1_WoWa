from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_UsersWindow
from .dialog_window import Dialog

from database import get_session, User, Character


class Users(QMainWindow, Ui_UsersWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.current_row = None

        self.push_goBack.clicked.connect(self.goBack)
        self.push_update.clicked.connect(self.update_table)
        self.push_BAN.clicked.connect(self.BAN)
        self.tableWidget_Users.cellClicked.connect(self.cellClicked)

        self.update_table()

    def update_table(self):
        print(self.item.text())
        if self.item.text() != "creator" and self.item.text() != "admin":
            self.push_BAN.hide()
        if self.item.text() == "creator" or self.item.text() == "admin":
            self.push_BAN.show()

        users = self.session.query(User).order_by(User.id).all()
        self.tableWidget_Users.setRowCount(0)
        for user in users:
            row_position = self.tableWidget_Users.rowCount()
            self.tableWidget_Users.insertRow(row_position)
            self.tableWidget_Users.setItem(row_position, 0, QTableWidgetItem(str(user.id)))
            self.tableWidget_Users.setItem(row_position, 1, QTableWidgetItem(user.username))

    def BAN(self):
        if self.current_row is None:
            return

        admunUserId = None
        users = self.session.query(User)
        for user in users:
            if user.username == self.item.text():
                admunUserId = user.id

        if int(self.tableWidget_Users.item(self.current_row, 0).text()) == admunUserId:
            dialog_window = Dialog("Вы не можете удалить себя.")
            a = dialog_window.exec_()
            return

        dialog_delete = Dialog("Точно хотите удалить?")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            user_id = int(self.tableWidget_Users.item(self.current_row, 0).text())
            user = self.session.query(User).get(user_id)

            characters = self.session.query(Character)
            for character in characters:
                if character.id_user == user_id:
                    characters.delete(character)
            self.session.commit()

            self.session.delete(user)
            self.session.commit()
            self.update_table()

    def cellClicked(self, row, column):
        self.current_row = row

    def showWindow(self):
        self.show()

    def goBack(self):
        self.close()