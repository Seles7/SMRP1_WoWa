from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_CharactersWindow
from .createCharacter_window import CreateCharacter

from database import get_session, Character, Race, Spec, RaceSpec, Guild, User

class Characters(QMainWindow, Ui_CharactersWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()

        self.push_goBackP.clicked.connect(self.goBack)
        self.push_CreateCharacter.clicked.connect(self.open_createCharacterWindow)
        self.push_update.clicked.connect(self.update_table)
        self.checkBox.clicked.connect(self.update_table)

        self.passTo_createCharacterWidget = CreateCharacter()

        self.update_table()

    def update_table(self):
        characters = self.session.query(Character).order_by(Character.id).all()
        users = self.session.query(User).order_by(User.id).all()
        guilds = self.session.query(Guild).order_by(Guild.id).all()
        races = self.session.query(Race).order_by(Race.id).all()
        specs = self.session.query(Spec).order_by(Spec.id).all()
        racesSpecs = self.session.query(RaceSpec).order_by(RaceSpec.id).all()

        isCheck = self.checkBox.isChecked()

        self.table_Characters.setRowCount(0)
        for character in characters:
            for user in users:
                if user.id == character.id_user:
                    user_ofChar = user.username

            if isCheck:
                if user_ofChar != self.item.text():
                    continue

            for raceSpec in racesSpecs:
                if raceSpec.id == character.id_racespec:
                    for race in races:
                        if race.id == raceSpec.race_id:
                            race_ofChar = race.title
                    for spec in specs:
                        if spec.id == raceSpec.spec_id:
                            spec_ofChar = spec.title
            for guild in guilds:
                if guild.id == character.id_guild:
                    guild_ofChar = guild.title

            row_position = self.table_Characters.rowCount()
            self.table_Characters.insertRow(row_position)
            self.table_Characters.setItem(row_position, 0, QTableWidgetItem(str(character.id)))
            self.table_Characters.setItem(row_position, 1, QTableWidgetItem(character.nickname))
            self.table_Characters.setItem(row_position, 2, QTableWidgetItem(str(race_ofChar)))
            self.table_Characters.setItem(row_position, 3, QTableWidgetItem(spec_ofChar))
            self.table_Characters.setItem(row_position, 4, QTableWidgetItem(str(character.level)))
            self.table_Characters.setItem(row_position, 5, QTableWidgetItem(guild_ofChar))
            self.table_Characters.setItem(row_position, 6, QTableWidgetItem(user_ofChar))

    def open_createCharacterWindow(self):
        self.passTo_createCharacterWidget.item.setText(self.item.text())
        self.passTo_createCharacterWidget.showWindow()

    def goBack(self):
        self.close()

    def showWindow(self):
        self.show()