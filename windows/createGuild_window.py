from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QComboBox, QDialog

from ui import Ui_CreateGuildWidget
from .dialog_window import Dialog

from database import get_session, Guild, Character, User


class CreateGuild(QWidget, Ui_CreateGuildWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.idNewGuild = -1

        self.push_CreateGuild.clicked.connect(self.createGuild)
        self.push_GoBack.clicked.connect(self.goBack)

        self.comboBox_character.clear()

    def updateComboBox(self):
        characters = self.session.query(Character)
        users = self.session.query(User)
        i_u = -1
        for user in users:
            if user.username == self.item.text():
                i_u = user.id
        for character in characters:
            if character.id_user == i_u:
                self.comboBox_character.addItem(character.nickname)

    def createGuild(self):
        titleIsFind = False
        nickname_input = self.comboBox_character.currentText()
        title_input = self.LineEdit_TitleGuild.text()

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
                if str(character.nickname) == str(nickname_input):
                    for guild in guilds:
                        if str(title_input) == str(guild.title):
                            exist_character: Character = self.session.query(Character).get(character.id)
                            exist_character.id_guild = int(guild.id)
                            print(guild.id)
                            print(int(character.id_guild))
                            self.session.commit()

                            dialog_warning = Dialog("Гильдия создана!")
                            dialog_warning.exec()

            self.custom_close()

    def open_invalidCreating(self):
        self.custom_close()

    def goBack(self):
        self.custom_close()

    def showWindow(self):
        if self.comboBox_character.currentText() == "":
            dialog_warning = Dialog("У вас нет ни одного персонажа! Вы не можете создать гильдию.")
            dialog_warning.exec()
            self.custom_close()
        else:
            self.show()

    def custom_close(self):
        self.close()