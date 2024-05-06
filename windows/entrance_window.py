from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem

from ui import Ui_EntranceWindow
from .registration_widget import Registration
from .authorization_widget import Authorization


from database import get_session


class EntranceWindow(QMainWindow, Ui_EntranceWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.SignUp.clicked.connect(self.create_RegistrationWidget)
        self.LogIn.clicked.connect(self.create_AuthorizationWidget)
        self.Exit.clicked.connect(self.exitFromWindow)
        self.key = list()
        self.key.append(0)


    def create_RegistrationWidget(self):
        self.create_window = Registration(self)
        self.create_window.show()

    def create_AuthorizationWidget(self):
        self.create_window = Authorization(self)
        self.create_window.show()
        self.close()

    def exitFromWindow(self):
        print(self.key)
        #self.close()

    def af(self):
        if(self.key == 1):
            self.close()
