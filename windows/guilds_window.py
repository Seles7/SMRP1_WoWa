from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_GuildsWindow

from database import get_session, Guild


class Guilds(QMainWindow, Ui_GuildsWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.update_table()

    def update_table(self):
        guilds = self.session.query(Guild).order_by(Guild.id).all()
        self.tableWidget_Guilds.setRowCount(0)
        for guild in guilds:
            row_position = self.tableWidget_Guilds.rowCount()
            self.tableWidget_Guilds.insertRow(row_position)
            self.tableWidget_Guilds.setItem(row_position, 0, QTableWidgetItem(str(guild.id)))
            self.tableWidget_Guilds.setItem(row_position, 1, QTableWidgetItem(guild.nickname))
            self.tableWidget_Guilds.setItem(row_position, 2, QTableWidgetItem())#число участников


    def showWindow(self):
        self.show()