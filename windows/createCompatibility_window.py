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