from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QDialog

from ui import Ui_CompatibilityWidget
from .dialog_window import Dialog

from database import get_session, Race, Spec, RaceSpec


class CreateCompatibility(QWidget, Ui_CompatibilityWidget):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.create_window = None
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_AceptCreate.clicked.connect(self.acceptCreateCompatibility)
        self.push_GoBack.clicked.connect(self.custom_close)

    def acceptCreateCompatibility(self):
        race_input = self.lineEdit_Race.text()
        spec_input = self.lineEdit_Spec.text()

        races = self.session.query(Race)
        specs = self.session.query(Spec)
        racesSpecs = self.session.query(RaceSpec)
        i_r = -1
        i_s = -1
        isFound = True
        if isFound:
            for race in races:
                if race_input == race.title:
                    i_r = race.id
                    print(i_r)
                    break
            if i_r == -1:
                isFound = False
        if isFound:
            for spec in specs:
                if spec_input == spec.title:
                    i_s = spec.id
                    break
            if i_s == -1:
                isFound = False
        if isFound:
            for raceSpec in racesSpecs:
                if i_s == raceSpec.race_id and i_r == raceSpec.spec_id:
                    isFound = False
                    break
        if isFound:
            new_compatibility = RaceSpec(race_id=i_r, spec_id=i_s)
            self.session.add(new_compatibility)
            self.session.commit()
            self.custom_close()

        if not isFound:
            self.open_compatibilityAlreadyRegist()

    def open_compatibilityAlreadyRegist(self):
        dialog_warning = Dialog("Некорректный Ввод! "
                                "Проверьте правильность написания расы и класса и убедитель, "
                                "что связи между ними нет.")
        dialog_warning.exec_()
        self.custom_close()

    def custom_close(self):
        self.close()