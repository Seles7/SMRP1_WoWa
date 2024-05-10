from typing import Iterable, Callable

from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import QDialog

from database import get_session
from ui import Ui_Dialog


class Dialog(QDialog, Ui_Dialog):
    def __init__(self, text: str):
        super().__init__()
        self.setupUi(self)
        self.textBrowser.setText(text)