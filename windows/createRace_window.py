from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_RaceWidget

from database import get_session, Race, Spec, RaceSpec

class racemake(QMainWindow, Ui_RaceWidget):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.update()

    class racemake(QMainWindow, Ui_RaceWidget):
        def __init__(self):
            super().__init__()
            self.create_window = None
            self.setupUi(self)
            self.session = get_session()
            self.item = QListWidgetItem()
            self.update()

        def createRace(self):
            race_input = self.lineEdit_Name.text()

            new_race = Race(title=race_input)

            for race in self.session:
                if str(new_race.title) == str(race.title):
                    self.open_specAlreadyRegist()

            self.session.add(new_race)
            self.session.commit()
            self.custom_close()

        def open_specAlreadyRegist(self):
            self.custom_close()

        def custom_close(self):
            self.close()