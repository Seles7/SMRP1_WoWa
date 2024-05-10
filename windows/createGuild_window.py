from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QDialog

from ui import Ui_CreateGuildWidget

from database import get_session, Guild, Character, User


class CreateGuild(QWidget, Ui_CreateGuildWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_GoBack.clicked.connect(self.goBack)

    def createGuild(self):
        nickname_input = self.LineEdit_Creator.text()
        title_input = self.LineEdit_TitleGuild.text()
        idUser = -1
        characterName = ""
        idUserGuild = -1

        characters = self.session.query(Character)
        users = self.session.query(User)
        guilds = self.session.query(Guild)

        for character in characters:
            if nickname_input == character.nickname:
                if idUser == character.id_user:
                    targetCharacter: Character =self.session.query(Character).get(character.id)
                else:
                    self.open_invalidCreating()
            else:
                self.open_invalidCreating()

        for guild in guilds:
            if title_input == guild.title:
                self.open_invalidCreating()
            else:
                targetCharacter.id_guild = guild.id
        new_guild = Guild(title=title_input)
        self.session.add(new_guild)
        self.session.commit()
        self.custom_close()

    def open_invalidCreating(self):
        self.custom_close()

    def goBack(self):
        self.close()

    def showWindow(self):
        self.show()