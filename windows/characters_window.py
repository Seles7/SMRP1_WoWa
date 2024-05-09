from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_CharactersWindow

from database import get_session, Character

class Characters(QMainWindow, Ui_CharactersWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()

        self.update_table()

    def update_table(self):
        characters = self.session.query(Character).order_by(Character.id).all()
        self.table_Characters.setRowCount(0)
        for character in characters:
             row_position = self.table_Characters.rowCount()
             self.table_Characters.insertRow(row_position)
             self.table_Characters.setItem(row_position, 0, QTableWidgetItem(str(character.id)))
             self.table_Characters.setItem(row_position, 1, QTableWidgetItem(character.nickname))
             self.table_Characters.setItem(row_position, 2, QTableWidgetItem())  # race
             self.table_Characters.setItem(row_position, 3, QTableWidgetItem())  # spec
             self.table_Characters.setItem(row_position, 4, QTableWidgetItem(character.level))
             self.table_Characters.setItem(row_position, 5, QTableWidgetItem(character.id_guild))
             self.table_Characters.setItem(row_position, 6, QTableWidgetItem(character.id_user))

    def exitFromWindow(self):
        self.close()

    def showWindow(self):
        self.show()