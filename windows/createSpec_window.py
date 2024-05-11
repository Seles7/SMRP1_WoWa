from typing import Iterable, Callable

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QListWidgetItem, QDialog

from ui import Ui_CreateSpecWidget

from database import get_session, Spec
from .dialog_window import Dialog


class CreateSpec(QWidget, Ui_CreateSpecWidget):
    def __init__(self, callbacks: Iterable[Callable]):
        super().__init__()
        self.create_window = None
        self.callbacks = callbacks
        self.setupUi(self)
        self.session = get_session()
        self.push_GoBack.clicked.connect(self.custom_close)
        self.push_AceptCreate.clicked.connect(self.acceptCreateRace)

    def acceptCreateRace(self):
        spec_input = self.lineEdit_Name.text()
        specs = self.session.query(Spec)
        key = False

        for spec in specs:
            if str(spec_input) == str(spec.title):
                key = True
                self.open_specAlreadyRegist()
        print(key)
        if not key:
            new_spec = Spec(title=spec_input)
            self.session.add(new_spec)
            self.session.commit()
            dialog_warning = Dialog("Класс успешно создан.")
            dialog_warning.exec_()
            self.custom_close()

    def open_specAlreadyRegist(self):
        dialog_warning = Dialog("Такой класс уже существует.")
        dialog_warning.exec_()
        self.custom_close()

    def custom_close(self):
        self.close()