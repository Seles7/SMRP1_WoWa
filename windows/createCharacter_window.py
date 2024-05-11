from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_CreateCharacterWidget

from database import get_session, Character, Race, Spec, RaceSpec, User


class CreateCharacter(QWidget, Ui_CreateCharacterWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_CreateCharacter.clicked.connect(self.createRace)
        self.push_GoBack.clicked.connect(self.custom_close)

    def createRace(self):
        nickname_input = self.LineEdit_Name.text()
        race_input = self.LineEdit_Race.text()
        spec_input = self.LineEdit_Spec.text()
        idUser = -1
        id_race = -1
        id_spec = -1
        idRaceSpec = -1

        characters = self.session.query(Character)
        users = self.session.query(User)
        races = self.session.query(Race)
        specs = self.session.query(Spec)
        racesSpecs = self.session.query(RaceSpec)

        for user in users:
            if str(self.item.text()) == str(user.username):
                idUser = user.id
        for race in races:
            if str(race_input) == str(race.title):
                id_race = race.id
        for spec in specs:
            if str(spec_input) == str(spec.title):
                id_spec = spec.id
        for raceSpec in racesSpecs:
            if raceSpec.race_id == id_race and raceSpec.spec_id == id_spec:
                idRaceSpec = raceSpec.id
            else:
                self.custom_close()

        for character in characters:
            if str(nickname_input) == str(character.nickname):
                self.custom_close()
        if idUser == -1 or id_race == -1 or id_spec == -1 or idRaceSpec == -1:
            self.custom_close()
        else:
            new_character = Character(nickname=nickname_input, level=1, id_user=idUser, id_racespec=idRaceSpec, id_guild=1)
            self.session.add(new_character)
            self.session.commit()
            self.custom_close()

    def open_userAlreadyRegist(self):
        self.custom_close()

    def custom_close(self):
        self.close()

    def showWindow(self):
        self.show()