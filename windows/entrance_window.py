from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog

from ui import UiEntranceWindow, UiRegistrationWindow, UiAuthorizationWindow
#from .registration_window import Registration

from database import get_session

class EntranceWindow(QMainWindow, UiEntranceWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        #self.LogIn.clicked.connect(self.open_registration())
        #self.SignUp.clicked.connect(self.open_authorization())

    #def open_registration(self):
        '''
        self.create_window = Registration()
        self.create_window.show()
        '''
    #def open_authorization(self):
        '''
        self.create_window = UiAuthorizationWindow()
        self.create_window.show()
        '''