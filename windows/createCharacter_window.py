from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_CreateCharacterWidget

from database import get_session, Character, Race, Spec, RaceSpec

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

        characters: Character = self.session.query(Character)
        races: Race = self.session.query(Race)
        specs: Spec = self.session.query(Spec)
        racesSpecs: RaceSpec = self.session.query(RaceSpec)

        for race in races:
            if str(race_input) == str(race.title):
                id_race = race.id
        for spec in specs:
            if str(spec_input) == str(spec.title):
                id_spec = spec.id
        for raceSpec in racesSpecs:
            if str(raceSpec.race_id) == id_race and raceSpec.spec_id == id_spec:
                idRaceSpec = raceSpec.id
            else:
                self.custom_close()

        for character in characters:
            if str(nickname_input) == str(character.nickname):
                self.custom_close()

            new_character = Character(nickname=nickname_input, level=1, id_raceSpec=idRaceSpec, id_guild=1)
            self.session.add(new_character)
            self.session.commit()
            self.custom_close()


    def open_userAlreadyRegist(self):
        self.custom_close()

    def custom_close(self):
        self.close()