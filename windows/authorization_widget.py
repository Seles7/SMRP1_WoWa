from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QDialog

from ui import Ui_AuthorizationWidget

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

    def enterUser(self):
        print("СЛАВА РОССИИ!")
        self.custom_close()

    def custom_close(self):
        #for callback in self.callbacks:
        #    callback()
        self.create_window = self.EntranceWindow()
        self.create_window.show()
        self.close()

