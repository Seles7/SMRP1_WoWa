from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QDialog

from ui import Ui_GuildsWindow

from database import get_session, Guild


class Guilds(QMainWindow, Ui_GuildsWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
