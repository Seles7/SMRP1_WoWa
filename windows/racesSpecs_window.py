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

        self.passTo_charactersWindow = Characters()
        self.passTo_usersWindow = Users()
        self.passTo_guildsWindow = Guilds()
        self.passTo_rasesSpecsWindow = RacesSpecs()


    def update_table(self):
        races = self.session.query(Race).order_by(Race.id).all()
        self.tableWidget_Races.setRowCount(0)
        for race in races:
            row_position = self.tableWidget_Races.rowCount()
            self.tableWidget_Races.insertRow(row_position)
            self.tableWidget_Races.setItem(row_position, 0, QTableWidgetItem(str(race.id)))
            self.tableWidget_Races.setItem(row_position, 1, QTableWidgetItem(race.nickname))

    def update_table(self):
        specs = self.session.query(Spec).order_by(Spec.id).all()
        self.tableWidget_Specs.setRowCount(0)
        for spec in specs:
            row_position = self.tableWidget_Specs.rowCount()
            self.tableWidget_Specs.insertRow(row_position)
            self.tableWidget_Specs.setItem(row_position, 0, QTableWidgetItem(str(spec.id)))
            self.tableWidget_Specs.setItem(row_position, 1, QTableWidgetItem(spec.nickname))


    def showWindow(self):
        self.show()

    def exitFromWindow(self):
        self.close()

    def openRaceMake(self):
        self.passTo_RaceMakeWindow.item.setText(self.item.text())
        self.passTo_RaceMakeWindow.showWindow()

    def openClassMake(self):
        self.passTo_ClassMakeWindow.item.setText(self.item.text())
        self.passTo_ClassMakeWindow.showWindow()

    def openSovmestimosti(self):
        self.passTo_SovmestimostiWindow.item.setText(self.item.text())
        self.passTo_SovmestimostiWindow.showWindow()