from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QMainWindow, QTableWidgetItem, QListWidgetItem, QDialog

from ui import Ui_ClassMake

from database import get_session, Race, Spec, RaceSpec

class classmake(QMainWindow, Ui_ClassMake):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.update()

    def createClass(self):
        spec_input = self.lineEdit_Name.text()

        new_spec = Spec(title=spec_input)

        for spec in self.session:
            if str(new_spec.title) == str(spec.title):
                self.open_specAlreadyRegist()

        self.session.add(new_spec)
        self.session.commit()
        self.custom_close()

    def open_specAlreadyRegist(self):
        self.custom_close()

    def custom_close(self):
        self.close()