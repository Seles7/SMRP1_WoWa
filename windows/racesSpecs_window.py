from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_RacesSpecsWindow

from database import get_session, Race, Spec, RaceSpec


class RacesSpecs(QMainWindow, Ui_RacesSpecsWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.update_table()

    def update_table(self):
        #races: Race = self.session.query(Race)
        #specs: Spec = self.session.query(Spec)
        racesSpecs: RaceSpec = self.session.query(RaceSpec)

        #races = self.session.query(Race).order_by(Race.id).all()

        self.tableWidget_RacesSpecs.setRowCount(0)

        for raceSpec in racesSpecs:
            race_inRacesSpecs = Race = self.session.query(Race).get(raceSpec.race_id)
            spec_inRacesSpecs = Spec = self.session.query(Spec).get(raceSpec.spec_id)

            row_position = self.tableWidget_Races.rowCount()
            self.tableWidget_Races.insertRow(row_position)
            self.tableWidget_Races.setItem(row_position, 0, QTableWidgetItem(str(race_inRacesSpecs.title)))
            self.tableWidget_Races.setItem(row_position, 1, QTableWidgetItem(str(spec_inRacesSpecs.title)))


    def showWindow(self):
        self.show()

    def exitFromWindow(self):
        self.close()
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