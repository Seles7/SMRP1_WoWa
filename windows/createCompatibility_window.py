from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QComboBox, QDialog

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

        self.comboBox_race.clear()
        self.comboBox_spec.clear()
        self.updateComboBoxes()

    def updateComboBoxes(self):
        races = self.session.query(Race)
        specs = self.session.query(Spec)
        for race in races:
            self.comboBox_race.addItem(race.title)
        for spec in specs:
            self.comboBox_spec.addItem(spec.title)

    def acceptCreateCompatibility(self):
        race_input = str(self.comboBox_race.currentText())
        spec_input = str(self.comboBox_spec.currentText())

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
                if i_r == raceSpec.race_id and i_s == raceSpec.spec_id:
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