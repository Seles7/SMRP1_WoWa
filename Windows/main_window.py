from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


from ui import UiMainWindow, UiCreateNewUser_Form
from database import get_session
from .create_user_window import UserCreate
from .store_window import Store


class MainWindow(QMainWindow, UiMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.new_user_button.clicked.connect(self.open_user_create)
        self.current_user_button.clicked.connect(self.open_store)

    def open_user_create(self):
        self.create_window = UserCreate(self)
        self.create_window.show()

    def open_store(self):
        self.create_window = Store()
        self.create_window.show()