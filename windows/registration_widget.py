from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QDialog

from ui import Ui_RegistrationWidget

from database import get_session, User
from .dialog_window import Dialog


class Registration(QWidget, Ui_RegistrationWidget):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.create_window = None
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_AceptRegist.clicked.connect(self.createUser)
        self.push_GoBack.clicked.connect(self.custom_close)

    def createUser(self):
        isFound = False
        username_input = self.lineEdit_Name.text()
        password_input = self.lineEdit_Password.text()

        new_user = User(username=username_input, password=password_input)

        users = self.session.query(User)
        for user in users:
            if str(new_user.username) == str(user.username):
                isFound = True
                self.open_userAlreadyRegist()

        if isFound == False:
            self.session.add(new_user)
            self.session.commit()
            self.custom_close()

    def open_userAlreadyRegist(self):
        dialog_warning = Dialog("Такой пользователь уже существует.")
        dialog_warning.exec_()
        self.custom_close()

    def custom_close(self):
        self.close()
