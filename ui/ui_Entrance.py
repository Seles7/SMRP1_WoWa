
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EntranceWindow(object):
    def setupUi(self, EntranceWindow):
        EntranceWindow.setObjectName("EntranceWindow")
        EntranceWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(EntranceWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.LogIn = QtWidgets.QPushButton(self.centralwidget)
        self.LogIn.setGeometry(QtCore.QRect(230, 190, 231, 61))
        self.LogIn.setObjectName("LogIn")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(40, 70, 531, 51))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.Title.setFont(font)
        self.Title.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Title.setObjectName("Title")
        self.Exit = QtWidgets.QPushButton(self.centralwidget)
        self.Exit.setGeometry(QtCore.QRect(230, 330, 231, 61))
        self.Exit.setObjectName("Exit")
        self.SignUp = QtWidgets.QPushButton(self.centralwidget)
        self.SignUp.setGeometry(QtCore.QRect(230, 260, 231, 61))
        self.SignUp.setObjectName("SignUp")
        EntranceWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(EntranceWindow)
        QtCore.QMetaObject.connectSlotsByName(EntranceWindow)

    def retranslateUi(self, EntranceWindow):
        _translate = QtCore.QCoreApplication.translate
        EntranceWindow.setWindowTitle(_translate("EntranceWindow", "Вход"))
        self.LogIn.setText(_translate("EntranceWindow", "Войти"))
        self.Title.setText(_translate("EntranceWindow", "Название"))
        self.Exit.setText(_translate("EntranceWindow", "Выйти из приложения"))
        self.SignUp.setText(_translate("EntranceWindow", "Регистрация"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EntranceWindow = QtWidgets.QMainWindow()
    ui = Ui_EntranceWindow()
    ui.setupUi(EntranceWindow)
    EntranceWindow.show()
    sys.exit(app.exec_())
