from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem

from ui import Ui_MainMenuWindow

from .characters_window import Characters
from .

from database import get_session


class MainMenu(QMainWindow, Ui_MainMenuWindow):
    def __init__(self):
        super().__init__()
        self.create_window = None
        self.setupUi(self)
        self.session = get_session()
        self.item = QListWidgetItem()
        self.push_Characters.clicked.connect(self.openHeroes)
        self.push_players.clicked.connect(self.openPlayers)
        self.push_Guilds.clicked.connect(self.openGuilds)
        self.push_RacesSpecs.clicked.connect(self.openRacesSpecs)

    def openHeroes(self):
        pass

    def openPlayers(self):
        pass

    def openGuilds(self):
        pass

    def openRacesSpecs(self):
        pass

    def showWindow(self):
        self.show()