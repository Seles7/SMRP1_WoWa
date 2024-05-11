import random
from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_ChangeCharacterWidget
from .createCharacter_window import CreateCharacter
from .dialog_window import Dialog

from database import get_session, Character, Race, Spec, RaceSpec, Guild, User

class ChangeCharacter(QWidget, Ui_ChangeCharacterWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.targetChar = self.session.query(Character).get(1)

        self.push_levelUp.clicked.connect(self.levelUp)
        self.push_changeGuild.clicked.connect(self.changeGuild)
        self.push_GoBack.clicked.connect(self.custom_close)
        self.push_delete.clicked.connect(self.deleteCharacter)

    def updateRecords(self):
        self.comboBox.clear()
        self.label_level.setText(str(self.targetChar.level))
        guilds = self.session.query(Guild)
        for guild in guilds:
            if guild.id == int(str(self.targetChar.id_guild)):
                self.comboBox.addItem(guild.title)
                break
        for guild in guilds:
            if guild.id != int(str(self.targetChar.id_guild)):
                self.comboBox.addItem(guild.title)

    def targetingCharacter(self):
        self.targetChar = self.session.query(Character).get(int(self.item.text()))
        self.updateRecords()

    def levelUp(self):
        if int(str(self.targetChar.level)) < 100:
            chanceSuccess = 100 - self.targetChar.level / 100 * 80
            chanceFail = self.targetChar.level / 100 * 20
            currentChance = random.randint(1, 100)
            if currentChance <= chanceSuccess:
                self.targetChar.level += 1
                self.session.commit()
                self.updateRecords()
                dialog_warning = Dialog("Вам повезло! Уровень поднят!")
                dialog_warning.exec_()
            elif chanceSuccess < currentChance and currentChance <= chanceFail:
                dialog_warning = Dialog("Опа! Уровень не изменён(")
                dialog_warning.exec_()
            else:
                dialog_warning = Dialog("Ого! Непавезо... Уровень понижен(((")
                dialog_warning.exec_()
        else:
            dialog_warning = Dialog("Ничего себе! Вы дослигли максимального уровня!")
            dialog_warning.exec_()

    def changeGuild(self):
        guild_input = str(self.comboBox.currentText())
        guilds = self.session.query(Guild)
        for guild in guilds:
            if guild_input == guild.title:
                if guild.id == int(str(self.targetChar.id_guild)):
                    dialog_warning = Dialog("Ваш персонаж уже состоит в этой гильдии.")
                    ret_value = dialog_warning.exec_()
                    return
                else:
                    dialog_warning = Dialog("Ваш персонаж успешно сменил гильдию!")
                    ret_value = dialog_warning.exec_()
                    self.targetChar.id_guild = guild.id
                    self.session.commit()

    def deleteCharacter(self):
        dialog_delete = Dialog("Точно хотите удалить персонажа?")
        ret_value = dialog_delete.exec_()
        if ret_value == QDialog.Accepted:
            self.session.delete(self.targetChar)
            self.session.commit()
            self.custom_close()

    def showWindow(self):
        self.show()

    def custom_close(self):
        self.comboBox.clear()
        self.close()
