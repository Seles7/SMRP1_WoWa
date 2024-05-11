from typing import Iterable, Callable
import time

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
        self.push_update.clicked.connect(self.update_table)
        self.push_goBack.clicked.connect(self.goBack)

        self.passTo_createGuildWindow = CreateGuild()

        self.update_table()

    def update_table(self):
        guilds = self.session.query(Guild).order_by(Guild.id).all()
        characters = self.session.query(Character).order_by(Character.id).all()

        self.tableWidget_Guilds.setRowCount(0)
        for guild in guilds:
            count = 0
            for character in characters:
                if character.id_guild == guild.id:
                    count += 1
            row_position = self.tableWidget_Guilds.rowCount()
            self.tableWidget_Guilds.insertRow(row_position)
            self.tableWidget_Guilds.setItem(row_position, 0, QTableWidgetItem(str(guild.id)))
            self.tableWidget_Guilds.setItem(row_position, 1, QTableWidgetItem(str(guild.title)))
            self.tableWidget_Guilds.setItem(row_position, 2, QTableWidgetItem(str(count)))

    def open_createGuildWindow(self):
        self.passTo_createGuildWindow.item.setText(self.item.text())
        self.passTo_createGuildWindow.updateComboBox()
        self.passTo_createGuildWindow.showWindow()

    def goBack(self):
        self.close()

    def showWindow(self):
        self.show()