from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QDialog

from ui import Ui_CreateRaceWidget

from database import get_session, Race


class CreateRace(QWidget, Ui_CreateRaceWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_GoBack.clicked.connect(self.custom_close)
        self.push_AceptCreate.clicked.connect(self.acceptCreateRace)

    def acceptCreateRace(self):
        race_input = self.lineEdit_Name.text()
        key = 1

        for race in self.session:
            if str(race_input) == str(race.title):
                self.open_specAlreadyRegist()

        new_race = Race(title=race_input)
        self.session.add(new_race)
        self.session.commit()
        self.custom_close()

    def open_specAlreadyRegist(self):
        self.custom_close()

    def custom_close(self):
        self.close()