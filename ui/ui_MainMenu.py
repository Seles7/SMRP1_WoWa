
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_ExitFromAccount = QtWidgets.QPushButton(self.centralwidget)
        self.push_ExitFromAccount.setGeometry(QtCore.QRect(30, 370, 201, 61))
        self.push_ExitFromAccount.setObjectName("push_ExitFromAccount")
        self.push_Guilds = QtWidgets.QPushButton(self.centralwidget)
        self.push_Guilds.setGeometry(QtCore.QRect(30, 210, 201, 61))
        self.push_Guilds.setObjectName("push_Guilds")
        self.push_Characters = QtWidgets.QPushButton(self.centralwidget)
        self.push_Characters.setGeometry(QtCore.QRect(30, 140, 201, 61))
        self.push_Characters.setObjectName("push_Characters")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(30, 30, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.push_RacesSpecs = QtWidgets.QPushButton(self.centralwidget)
        self.push_RacesSpecs.setGeometry(QtCore.QRect(30, 280, 201, 61))
        self.push_RacesSpecs.setObjectName("push_RacesSpecs")
        MainMenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "Главное меню"))
        self.push_ExitFromAccount.setText(_translate("MainMenuWindow", "Выйти из аккаунта"))
        self.push_Guilds.setText(_translate("MainMenuWindow", "Гильдии"))
        self.push_Characters.setText(_translate("MainMenuWindow", "Персонажи"))
        self.Title.setText(_translate("MainMenuWindow", "Главное меню"))
        self.push_RacesSpecs.setText(_translate("MainMenuWindow", "Расы и Классы"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec_())
