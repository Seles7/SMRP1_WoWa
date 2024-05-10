from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QDialog

from ui import Ui_EntranceWindow
from .registration_widget import Registration
from .authorization_widget import Authorization
from .dialog_window import Dialog


from database import get_session


class Entrance(QMainWindow, Ui_EntranceWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.SignUp.clicked.connect(self.create_RegistrationWidget)
        self.LogIn.clicked.connect(self.create_AuthorizationWidget)
        self.Exit.clicked.connect(self.exitFromWindow)

    def create_RegistrationWidget(self):
        self.create_window = Registration(self)
        self.create_window.show()

    def create_AuthorizationWidget(self):
        self.create_window = Authorization(self)
        self.create_window.show()

    def exitFromWindow(self):
        dialog_warning = Dialog("Вы уверены что хотите выйти?")
        ret_value = dialog_warning.exec_()
        if ret_value == QDialog.Accepted:
            self.custom_close()