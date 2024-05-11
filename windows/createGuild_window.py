from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QComboBox, QDialog

from ui import Ui_CreateGuildWidget

from database import get_session, Guild, Character, User


class CreateGuild(QWidget, Ui_CreateGuildWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()

        self.push_CreateGuild.clicked.connect(self.createGuild)
        self.push_GoBack.clicked.connect(self.goBack)

        self.comboBox_character.clear()

    def updateComboBox(self):
        characters = self.session.query(Character)
        users = self.session.query(User)
        print()
        print(self.item.text())
        print()
        i_u = -1
        for user in users:
            if user.username == self.item.text():
                i_u = user.id
        for character in characters:
            if character.id_user == i_u:
                self.comboBox_character.addItem(character.nickname)

    def createGuild(self):
        print()
        print(self.item.text())
        print()
        titleIsFind = False
        nickname_input = self.comboBox_character.currentText()
        title_input = self.LineEdit_TitleGuild.text()
        idGuild = -1

        characters = self.session.query(Character)
        guilds = self.session.query(Guild)

        for guild in guilds:
            if title_input == guild.title:
                titleIsFind = True
                self.open_invalidCreating()

        if not titleIsFind:
            new_guild = Guild(title=title_input)
            self.session.add(new_guild)
            self.session.commit()

            for character in characters:
                if character.nickname == nickname_input:
                    for guild in guilds:
                        if guild.id == idGuild:
                            character.id_guild = idGuild
                            self.session.commit()

            self.custom_close()

    def open_invalidCreating(self):
        self.custom_close()

    def goBack(self):
        self.close()

    def showWindow(self):
        self.show()

    def custom_close(self):
        self.close()