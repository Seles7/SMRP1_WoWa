from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_RacesSpecsWindow
#from .createRace_window import

from database import get_session, Race, Spec, RaceSpec


class RacesSpecs(QMainWindow, Ui_RacesSpecsWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()

        self.push_goBack.clicked.connect(self.exitFromWindow)
        self.push_addRace.clicked.connect(self.exitFromWindow)
        self.push_addSpec.clicked.connect(self.exitFromWindow)
        self.push_addRaceSpec.clicked.connect(self.exitFromWindow)

        #self.passTo_createRaceWindow = Cre(

        self.update_table()

    def update_table(self):
        races: Race = self.session.query(Race)
        specs: Spec = self.session.query(Spec)
        racesSpecs: RaceSpec = self.session.query(RaceSpec)

        self.tableWidget_Races.setRowCount(0)
        for race in races:
            row_position = self.tableWidget_RacesSpecs.rowCount()
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
                if(raceSpec.race_id == race.id):
                    race_inRacesSpecs = race.title
            for spec in specs:
                if (raceSpec.spec_id == spec.id):
                    spec_inRacesSpecs = spec.title

            row_position = self.tableWidget_RacesSpecs.rowCount()
            self.tableWidget_RacesSpecs.insertRow(row_position)
            self.tableWidget_RacesSpecs.setItem(row_position, 0, QTableWidgetItem(str(race_inRacesSpecs)))
            self.tableWidget_RacesSpecs.setItem(row_position, 1, QTableWidgetItem(str(spec_inRacesSpecs)))

    def showWindow(self):
        self.show()

    def exitFromWindow(self):
        self.close()

'''
    def openCreateRaceWindow(self):
        self.passTo_SovmestimostiWindow.item.setText(self.item.text())
        self.passTo_SovmestimostiWindow.showWindow()

    def openCreateSpecWindow(self):
        pass

    def openCreateRaceSpecWindow(self):
        pass
'''
'''
    def openRaceMake(self):
        self.passTo_RaceMakeWindow.item.setText(self.item.text())
        self.passTo_RaceMakeWindow.showWindow()

    def openClassMake(self):
        self.passTo_ClassMakeWindow.item.setText(self.item.text())
        self.passTo_ClassMakeWindow.showWindow()

    def openSovmestimosti(self):
        self.passTo_SovmestimostiWindow.item.setText(self.item.text())
        self.passTo_SovmestimostiWindow.showWindow()
        '''