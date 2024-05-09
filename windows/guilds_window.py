from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_GuildsWindow
from .createGuild_window import CreateGuild

from database import get_session, Guild, Character


class Guilds(QMainWindow, Ui_GuildsWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_createGuild.clicked.connect(self.open_createGuildWindow)

        self.passTo_createGuildWindow = CreateGuild()

        #self.update_table()

    def open_createGuildWindow(self):
        self.passTo_createGuildWindow.item.setText(self.item.text())
        self.passTo_createGuildWindow.showWindow()

    def showWindow(self):
        self.show()