from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QDialog

from ui import Ui_CreateRaceWidget

from database import get_session, Race
from .dialog_window import Dialog


class CreateRace(QWidget, Ui_CreateRaceWidget):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.create_window = None
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_GoBack.clicked.connect(self.custom_close)
        self.push_AceptCreate.clicked.connect(self.acceptCreateRace)

    def acceptCreateRace(self):
        race_input = self.lineEdit_Name.text()
        races = self.session.query(Race)
        key = False

        for race in races:
            if str(race_input) == str(race.title):
                key = True
                self.open_raceAlreadyRegist()
        if not key:
            new_race = Race(title=race_input)
            self.session.add(new_race)
            self.session.commit()
            dialog_warning = Dialog("Раса успешно создана.")
            dialog_warning.exec_()
            self.custom_close()

    def open_raceAlreadyRegist(self):
        dialog_warning = Dialog("Такая раса уже существует.")
        dialog_warning.exec_()
        self.custom_close()

    def custom_close(self):
        self.close()