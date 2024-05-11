from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_RacesSpecsWindow
from .createRace_window import CreateRace
from .createSpec_window import CreateSpec
from .createCompatibility_window import CreateCompatibility

from database import get_session, Race, Spec, RaceSpec


class RacesSpecs(QMainWindow, Ui_RacesSpecsWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()

        self.push_addRace.clicked.connect(self.openCreateRaceWindow)
        self.push_addSpec.clicked.connect(self.openCreateSpecWindow)
        self.push_addRaceSpec.clicked.connect(self.openCreateRaceSpecWindow)
        self.push_update.clicked.connect(self.update_table)
        self.push_goBack.clicked.connect(self.exitFromWindow)

        self.update_table()

    def update_table(self):
        if self.item.text() != "creator" and self.item.text() != "developer":
            self.push_addRace.hide()
            self.push_addSpec.hide()
            self.push_addRaceSpec.hide()
        if self.item.text() == "creator" or self.item.text() == "developer":
            self.push_addRace.show()
            self.push_addSpec.show()
            self.push_addRaceSpec.show()

        races = self.session.query(Race).order_by(Race.id).all()
        specs = self.session.query(Spec).order_by(Spec.id).all()
        racesSpecs = self.session.query(RaceSpec).order_by(RaceSpec.race_id).all()

        self.tableWidget_Races.setRowCount(0)
        for race in races:
            row_position = self.tableWidget_Races.rowCount()
            self.tableWidget_Races.insertRow(row_position)
            self.tableWidget_Races.setItem(row_position, 0, QTableWidgetItem(str(race.id)))
            self.tableWidget_Races.setItem(row_position, 1, QTableWidgetItem(str(race.title)))

        self.tableWidget_Specs.setRowCount(0)
        for spec in specs:
            row_position = self.tableWidget_Specs.rowCount()
            self.tableWidget_Specs.insertRow(row_position)
            self.tableWidget_Specs.setItem(row_position, 0, QTableWidgetItem(str(spec.id)))
            self.tableWidget_Specs.setItem(row_position, 1, QTableWidgetItem(str(spec.title)))

        self.tableWidget_RacesSpecs.setRowCount(0)
        for raceSpec in racesSpecs:
            for race in races:
                if raceSpec.race_id == race.id:
                    race_inRacesSpecs = race.title
            for spec in specs:
                if raceSpec.spec_id == spec.id:
                    spec_inRacesSpecs = spec.title

            row_position = self.tableWidget_RacesSpecs.rowCount()
            self.tableWidget_RacesSpecs.insertRow(row_position)
            self.tableWidget_RacesSpecs.setItem(row_position, 0, QTableWidgetItem(str(race_inRacesSpecs)))
            self.tableWidget_RacesSpecs.setItem(row_position, 1, QTableWidgetItem(str(spec_inRacesSpecs)))

    def openCreateRaceWindow(self):
        self.create_window = CreateRace(self)
        self.create_window.show()

    def openCreateSpecWindow(self):
        self.create_window = CreateSpec(self)
        self.create_window.show()

    def openCreateRaceSpecWindow(self):
        self.create_window = CreateCompatibility(self)
        self.create_window.show()

    def showWindow(self):
        self.show()

    def exitFromWindow(self):
        self.update_table()
        self.close()

