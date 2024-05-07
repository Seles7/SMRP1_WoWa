# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\Users_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UsersWindow(object):
    def setupUi(self, UsersWindow):
        UsersWindow.setObjectName("UsersWindow")
        UsersWindow.resize(700, 500)
        UsersWindow.setMinimumSize(QtCore.QSize(700, 500))
        UsersWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(UsersWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(260, 10, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(32)
        self.Title.setFont(font)
        self.Title.setStyleSheet("")
        self.Title.setObjectName("Title")
        self.push_goBack = QtWidgets.QPushButton(self.centralwidget)
        self.push_goBack.setGeometry(QtCore.QRect(500, 440, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_goBack.setFont(font)
        self.push_goBack.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_goBack.setObjectName("push_goBack")
        self.tableWidget_Users = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Users.setEnabled(True)
        self.tableWidget_Users.setGeometry(QtCore.QRect(20, 60, 661, 371))
        self.tableWidget_Users.setStyleSheet("border-image: url(:/pins1/pergament4.jpg);")
        self.tableWidget_Users.setAutoScroll(True)
        self.tableWidget_Users.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Users.setShowGrid(True)
        self.tableWidget_Users.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget_Users.setWordWrap(True)
        self.tableWidget_Users.setRowCount(2)
        self.tableWidget_Users.setColumnCount(2)
        self.tableWidget_Users.setObjectName("tableWidget_Users")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Users.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Users.setHorizontalHeaderItem(1, item)
        self.tableWidget_Users.horizontalHeader().setVisible(True)
        self.tableWidget_Users.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Users.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Users.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_Users.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Users.verticalHeader().setVisible(True)
        self.tableWidget_Users.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Users.verticalHeader().setHighlightSections(True)
        self.tableWidget_Users.verticalHeader().setSortIndicatorShown(False)
        self.img_background = QtWidgets.QLabel(self.centralwidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 700, 500))
        self.img_background.setMinimumSize(QtCore.QSize(700, 500))
        self.img_background.setMaximumSize(QtCore.QSize(700, 500))
        self.img_background.setStyleSheet("")
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/tavern.jpg"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.img_underUsers = QtWidgets.QLabel(self.centralwidget)
        self.img_underUsers.setGeometry(QtCore.QRect(230, 10, 201, 41))
        self.img_underUsers.setText("")
        self.img_underUsers.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underUsers.setScaledContents(True)
        self.img_underUsers.setObjectName("img_underUsers")
        self.push_BAN = QtWidgets.QPushButton(self.centralwidget)
        self.push_BAN.setGeometry(QtCore.QRect(30, 440, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_BAN.setFont(font)
        self.push_BAN.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_BAN.setObjectName("push_BAN")
        self.img_background.raise_()
        self.img_underUsers.raise_()
        self.Title.raise_()
        self.push_goBack.raise_()
        self.tableWidget_Users.raise_()
        self.push_BAN.raise_()
        UsersWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(UsersWindow)
        QtCore.QMetaObject.connectSlotsByName(UsersWindow)

    def retranslateUi(self, UsersWindow):
        _translate = QtCore.QCoreApplication.translate
        UsersWindow.setWindowTitle(_translate("UsersWindow", "Игроки"))
        self.Title.setText(_translate("UsersWindow", "Игроки"))
        self.push_goBack.setText(_translate("UsersWindow", "Назад"))
        self.tableWidget_Users.setSortingEnabled(False)
        item = self.tableWidget_Users.horizontalHeaderItem(0)
        item.setText(_translate("UsersWindow", "id"))
        item = self.tableWidget_Users.horizontalHeaderItem(1)
        item.setText(_translate("UsersWindow", "Никнейм"))
        self.push_BAN.setText(_translate("UsersWindow", "Забанить"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UsersWindow = QtWidgets.QMainWindow()
    ui = Ui_UsersWindow()
    ui.setupUi(UsersWindow)
    UsersWindow.show()
    sys.exit(app.exec_())
