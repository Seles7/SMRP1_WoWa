from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QMainWindow, QListWidgetItem, QDialog

from ui import Ui_MainMenuWindow

from .characters_window import Characters
from .users_window import Users
from .guilds_window import Guilds
from .racesSpecs_window import RacesSpecs
from .dialog_window import Dialog

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
        self.push_ExitFromAccount.clicked.connect(self.exitFromAccount)

        self.passTo_charactersWindow = Characters()
        self.passTo_usersWindow = Users()
        self.passTo_guildsWindow = Guilds()
        self.passTo_rasesSpecsWindow = RacesSpecs()

    def openHeroes(self):
        self.passTo_charactersWindow.item.setText(self.item.text())
        self.passTo_charactersWindow.showWindow()

    def openPlayers(self):
        self.passTo_usersWindow.item.setText(self.item.text())
        self.passTo_usersWindow.pushVision()
        self.passTo_usersWindow.showWindow()

    def openGuilds(self):
        self.passTo_guildsWindow.item.setText(self.item.text())
        self.passTo_guildsWindow.pushVision()
        self.passTo_guildsWindow.showWindow()

    def openRacesSpecs(self):
        self.passTo_rasesSpecsWindow.item.setText(self.item.text())
        self.passTo_rasesSpecsWindow.pushVision()
        self.passTo_rasesSpecsWindow.update_all()
        self.passTo_rasesSpecsWindow.showWindow()

    def exitFromAccount(self):
        dialog_warning = Dialog("Вы уверены, что хотите выйти?")
        ret_value = dialog_warning.exec_()
        if ret_value == QDialog.Accepted:
            self.custom_close()

    def showWindow(self):
        print(self.item.text())
        self.label_username.setText(self.item.text())
        self.show()

    def custom_close(self):
        self.close()