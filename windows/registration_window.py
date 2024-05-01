from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QDialog

from ui import UiEntranceWindow, UiRegistrationWindow

from database import get_session, User

'''from typing import Iterable, Callable
from PyQt5.QtWidgets import QWidget

from ui import UiCreateNewUser_Form
from database import get_session, User
from .user_already_exists import UserAlreadyExists'''

class Registration(QWidget, UiRegistrationWindow):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.create_window = None
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_AceptRegist.clicked.connect(self.registration)

    def registration(self):
        '''
        username_input = self.lineEdit.text()
        new_user = User(nickname=username_input)
        print(new_user)
        all_users = self.session.query(User).all()
        print(all_users)
        all_nicknames = []
        for i in range(len(all_users)):
            user_check: User = self.session.query(User).get(i+1)
            print(user_check)
            nick = user_check.nickname
            all_nicknames.append(nick)
        print(all_nicknames)
        if new_user.nickname not in all_nicknames:
            self.session.add(new_user)
            self.session.commit()
            self.close()
        else:
            self.open_user_already_exists()

    def custom_close(self):
        for callback in self.callbacks:
            callback()
        self.close()


    def open_user_already_exists(self):
        self.create_window = UserAlreadyExists()
        self.create_window.show()
    '''