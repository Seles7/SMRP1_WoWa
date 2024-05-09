from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_CreateCharacterWidget

from database import get_session, Character

class CreateCharacter(QWidget, Ui_CreateCharacterWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_CreateCharacter.clicked.connect(self.create)

    def create(self):
        nickname_input = self.LineEdit_Name.text()
        race_input = self.LineEdit_Race.text()
        spec_input = self.LineEdit_Spec.text()


        new_character = Character(nickname=nickname_input, race=race_input, spec=spec_input)

        users: User = self.session.query(User)

        for user in users:
            if str(new_user.username) == str(user.username) \
                    and str(new_user.password) == str(user.password):
                self.passTo_mainWindow.item.setText(new_user.username)
                self.passTo_mainWindow.showWindow()
                self.custom_close()
        self.open_userAlreadyRegist()

    def open_userAlreadyRegist(self):
        self.custom_close()

    def custom_close(self):
        self.close()