from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_CompatibilityWidget

from database import get_session, Race, Spec, RaceSpec


class CreateCompatibility(QWidget, Ui_CompatibilityWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()

    def acceptCreateRace(self):
        race_input = self.lineEdit_Name.text()
        key = 1

        for race in self.session:
            if str(race_input) == str(race.title):
                key = 0
                self.open_raceAlreadyRegist()
        if key == 1:
            new_race = Race(title=race_input)
            self.session.add(new_race)
            self.session.commit()
            self.custom_close()

    def open_raceAlreadyRegist(self):
        dialog_warning = Dialog("Такая раса уже существует.")
        dialog_warning.exec_()
        self.custom_close()

    def custom_close(self):
        self.close()