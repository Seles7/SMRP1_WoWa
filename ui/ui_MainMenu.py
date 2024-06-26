# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\MainMenu_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainMenuWindow(object):
    def setupUi(self, MainMenuWindow):
        MainMenuWindow.setObjectName("MainMenuWindow")
        MainMenuWindow.resize(700, 500)
        MainMenuWindow.setMinimumSize(QtCore.QSize(700, 500))
        MainMenuWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(MainMenuWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_ExitFromAccount = QtWidgets.QPushButton(self.centralwidget)
        self.push_ExitFromAccount.setGeometry(QtCore.QRect(70, 459, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.push_ExitFromAccount.setFont(font)
        self.push_ExitFromAccount.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_ExitFromAccount.setObjectName("push_ExitFromAccount")
        self.push_Guilds = QtWidgets.QPushButton(self.centralwidget)
        self.push_Guilds.setGeometry(QtCore.QRect(70, 360, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_Guilds.setFont(font)
        self.push_Guilds.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_Guilds.setObjectName("push_Guilds")
        self.push_Characters = QtWidgets.QPushButton(self.centralwidget)
        self.push_Characters.setGeometry(QtCore.QRect(70, 280, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_Characters.setFont(font)
        self.push_Characters.setAutoFillBackground(False)
        self.push_Characters.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)\n"
"")
        self.push_Characters.setAutoDefault(False)
        self.push_Characters.setDefault(False)
        self.push_Characters.setFlat(False)
        self.push_Characters.setObjectName("push_Characters")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(270, 10, 171, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(31)
        self.Title.setFont(font)
        self.Title.setStyleSheet("")
        self.Title.setObjectName("Title")
        self.push_RacesSpecs = QtWidgets.QPushButton(self.centralwidget)
        self.push_RacesSpecs.setGeometry(QtCore.QRect(70, 400, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_RacesSpecs.setFont(font)
        self.push_RacesSpecs.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_RacesSpecs.setObjectName("push_RacesSpecs")
        self.img_background = QtWidgets.QLabel(self.centralwidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.img_background.setMinimumSize(QtCore.QSize(700, 500))
        self.img_background.setMaximumSize(QtCore.QSize(700, 500))
        self.img_background.setStyleSheet("background-image: url(:/newPrefix/Desktop/Прочее/MainMenu.png);")
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/zastavochka.png"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.push_players = QtWidgets.QPushButton(self.centralwidget)
        self.push_players.setGeometry(QtCore.QRect(70, 320, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_players.setFont(font)
        self.push_players.setAutoFillBackground(False)
        self.push_players.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)\n"
"")
        self.push_players.setAutoDefault(False)
        self.push_players.setDefault(False)
        self.push_players.setFlat(False)
        self.push_players.setObjectName("push_players")
        self.img_underGopika = QtWidgets.QLabel(self.centralwidget)
        self.img_underGopika.setGeometry(QtCore.QRect(230, 10, 251, 61))
        self.img_underGopika.setText("")
        self.img_underGopika.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underGopika.setScaledContents(True)
        self.img_underGopika.setObjectName("img_underGopika")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 240, 191, 31))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_username = QtWidgets.QLabel(self.centralwidget)
        self.label_username.setGeometry(QtCore.QRect(80, 250, 131, 16))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.label_username.setFont(font)
        self.label_username.setFocusPolicy(QtCore.Qt.NoFocus)
        self.label_username.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.label_username.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_username.setText("")
        self.label_username.setObjectName("label_username")
        self.img_background.raise_()
        self.img_underGopika.raise_()
        self.push_ExitFromAccount.raise_()
        self.push_Guilds.raise_()
        self.push_Characters.raise_()
        self.Title.raise_()
        self.push_RacesSpecs.raise_()
        self.push_players.raise_()
        self.label.raise_()
        self.label_username.raise_()
        MainMenuWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainMenuWindow)
        QtCore.QMetaObject.connectSlotsByName(MainMenuWindow)

    def retranslateUi(self, MainMenuWindow):
        _translate = QtCore.QCoreApplication.translate
        MainMenuWindow.setWindowTitle(_translate("MainMenuWindow", "Главное меню"))
        self.push_ExitFromAccount.setText(_translate("MainMenuWindow", "Выйти из аккаунта"))
        self.push_Guilds.setText(_translate("MainMenuWindow", "Гильдии"))
        self.push_Characters.setText(_translate("MainMenuWindow", "Герои"))
        self.Title.setText(_translate("MainMenuWindow", "Гопика 3.5"))
        self.push_RacesSpecs.setText(_translate("MainMenuWindow", "Расы и Классы"))
        self.push_players.setText(_translate("MainMenuWindow", "Игроки"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainMenuWindow = QtWidgets.QMainWindow()
    ui = Ui_MainMenuWindow()
    ui.setupUi(MainMenuWindow)
    MainMenuWindow.show()
    sys.exit(app.exec_())
