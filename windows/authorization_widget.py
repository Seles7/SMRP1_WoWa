from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog

from ui import Ui_AuthorizationWidget
from .mainMenu_window import MainMenu
from .dialog_window import Dialog

from database import get_session, User


class Authorization(QWidget, Ui_AuthorizationWidget):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.create_window = None
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_AceptAuthoriz.clicked.connect(self.enterUser)
        self.push_GoBack.clicked.connect(self.custom_close)
        self.passTo_mainWindow = MainMenu()

    def enterUser(self):
        self.isFind = False
        username_input = self.lineEdit_Name.text()
        password_input = self.lineEdit_Password.text()

        new_user = User(username=username_input, password=password_input)

        users = self.session.query(User)

        for user in users:
            print(type(user.id))
            if str(new_user.username) == str(user.username) \
                    and str(new_user.password) == str(user.password):
                self.isFind = True
                self.passTo_mainWindow.item.setText(new_user.username)
                self.passTo_mainWindow.showWindow()
                self.custom_close()

        if self.isFind == False:
            self.open_userInvalidInput()

    def open_userInvalidInput(self):
        dialog_warning = Dialog("Некорректный ввод! Проверьте правильность ввода данных.")
        dialog_warning.exec_()
        self.custom_close()

    def custom_close(self):
        self.close()

