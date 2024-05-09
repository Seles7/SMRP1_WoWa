from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QListWidgetItem, QDialog

from ui import Ui_CreateGuildWidget

from database import get_session, Guild, Character


class CreateGuild(QMainWindow, Ui_CreateGuildWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()


    def showWindow(self):
        self.show()