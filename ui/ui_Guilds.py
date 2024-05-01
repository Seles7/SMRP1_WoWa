
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GuildsWindow(object):
    def setupUi(self, GuildsWindow):
        GuildsWindow.setObjectName("GuildsWindow")
        GuildsWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(GuildsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_createGuild = QtWidgets.QPushButton(self.centralwidget)
        self.push_createGuild.setGeometry(QtCore.QRect(20, 440, 171, 41))
        self.push_createGuild.setObjectName("push_createGuild")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(30, 10, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.push_goBack = QtWidgets.QPushButton(self.centralwidget)
        self.push_goBack.setGeometry(QtCore.QRect(500, 440, 171, 41))
        self.push_goBack.setObjectName("push_goBack")
        self.tableWidget_Guilds = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Guilds.setGeometry(QtCore.QRect(10, 60, 671, 371))
        self.tableWidget_Guilds.setObjectName("tableWidget_Guilds")
        self.tableWidget_Guilds.setColumnCount(3)
        self.tableWidget_Guilds.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Guilds.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Guilds.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Guilds.setHorizontalHeaderItem(2, item)
        GuildsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(GuildsWindow)
        QtCore.QMetaObject.connectSlotsByName(GuildsWindow)

    def retranslateUi(self, GuildsWindow):
        _translate = QtCore.QCoreApplication.translate
        GuildsWindow.setWindowTitle(_translate("GuildsWindow", "Гильдии"))
        self.push_createGuild.setText(_translate("GuildsWindow", "Создать гильдию"))
        self.Title.setText(_translate("GuildsWindow", "Гильдии"))
        self.push_goBack.setText(_translate("GuildsWindow", "Назад"))
        item = self.tableWidget_Guilds.horizontalHeaderItem(0)
        item.setText(_translate("GuildsWindow", "id"))
        item = self.tableWidget_Guilds.horizontalHeaderItem(1)
        item.setText(_translate("GuildsWindow", "Название"))
        item = self.tableWidget_Guilds.horizontalHeaderItem(2)
        item.setText(_translate("GuildsWindow", "Число участников"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GuildsWindow = QtWidgets.QMainWindow()
    ui = Ui_GuildsWindow()
    ui.setupUi(GuildsWindow)
    GuildsWindow.show()
    sys.exit(app.exec_())
