# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\RacesSpecs_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RacesSpecsWindow(object):
    def setupUi(self, RacesSpecsWindow):
        RacesSpecsWindow.setObjectName("RacesSpecsWindow")
        RacesSpecsWindow.resize(700, 500)
        RacesSpecsWindow.setMinimumSize(QtCore.QSize(700, 500))
        RacesSpecsWindow.setMaximumSize(QtCore.QSize(700, 500))
        self.centralwidget = QtWidgets.QWidget(RacesSpecsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(240, 20, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(29)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.tableWidget_Races = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Races.setGeometry(QtCore.QRect(20, 110, 211, 271))
        self.tableWidget_Races.setStyleSheet("border-image: url(:/pins1/pergament4.jpg);")
        self.tableWidget_Races.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Races.setObjectName("tableWidget_Races")
        self.tableWidget_Races.setColumnCount(2)
        self.tableWidget_Races.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Races.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Races.setHorizontalHeaderItem(1, item)
        self.tableWidget_Races.horizontalHeader().setStretchLastSection(False)
        self.label_Races = QtWidgets.QLabel(self.centralwidget)
        self.label_Races.setGeometry(QtCore.QRect(100, 80, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.label_Races.setFont(font)
        self.label_Races.setObjectName("label_Races")
        self.label_RacesSpecs = QtWidgets.QLabel(self.centralwidget)
        self.label_RacesSpecs.setGeometry(QtCore.QRect(540, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.label_RacesSpecs.setFont(font)
        self.label_RacesSpecs.setObjectName("label_RacesSpecs")
        self.tableWidget_Specs = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_Specs.setGeometry(QtCore.QRect(240, 110, 211, 271))
        self.tableWidget_Specs.setStyleSheet("border-image: url(:/pins1/pergament4.jpg);")
        self.tableWidget_Specs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_Specs.setObjectName("tableWidget_Specs")
        self.tableWidget_Specs.setColumnCount(2)
        self.tableWidget_Specs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Specs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Specs.setHorizontalHeaderItem(1, item)
        self.tableWidget_Specs.horizontalHeader().setStretchLastSection(False)
        self.push_addRace = QtWidgets.QPushButton(self.centralwidget)
        self.push_addRace.setGeometry(QtCore.QRect(70, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_addRace.setFont(font)
        self.push_addRace.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_addRace.setObjectName("push_addRace")
        self.label_Specs = QtWidgets.QLabel(self.centralwidget)
        self.label_Specs.setGeometry(QtCore.QRect(310, 80, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.label_Specs.setFont(font)
        self.label_Specs.setObjectName("label_Specs")
        self.tableWidget_RacesSpecs = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_RacesSpecs.setGeometry(QtCore.QRect(460, 110, 221, 271))
        self.tableWidget_RacesSpecs.setStyleSheet("border-image: url(:/pins1/pergament4.jpg);")
        self.tableWidget_RacesSpecs.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_RacesSpecs.setObjectName("tableWidget_RacesSpecs")
        self.tableWidget_RacesSpecs.setColumnCount(2)
        self.tableWidget_RacesSpecs.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RacesSpecs.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_RacesSpecs.setHorizontalHeaderItem(1, item)
        self.tableWidget_RacesSpecs.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_RacesSpecs.horizontalHeader().setStretchLastSection(True)
        self.push_addSpec = QtWidgets.QPushButton(self.centralwidget)
        self.push_addSpec.setGeometry(QtCore.QRect(290, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_addSpec.setFont(font)
        self.push_addSpec.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_addSpec.setObjectName("push_addSpec")
        self.push_goBack = QtWidgets.QPushButton(self.centralwidget)
        self.push_goBack.setGeometry(QtCore.QRect(540, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_goBack.setFont(font)
        self.push_goBack.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_goBack.setObjectName("push_goBack")
        self.push_addRaceSpec = QtWidgets.QPushButton(self.centralwidget)
        self.push_addRaceSpec.setGeometry(QtCore.QRect(510, 390, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_addRaceSpec.setFont(font)
        self.push_addRaceSpec.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_addRaceSpec.setObjectName("push_addRaceSpec")
        self.img_background = QtWidgets.QLabel(self.centralwidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 701, 501))
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/heroes.jpg"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.img_underRacesSpecs = QtWidgets.QLabel(self.centralwidget)
        self.img_underRacesSpecs.setGeometry(QtCore.QRect(200, 20, 291, 51))
        self.img_underRacesSpecs.setText("")
        self.img_underRacesSpecs.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underRacesSpecs.setScaledContents(True)
        self.img_underRacesSpecs.setObjectName("img_underRacesSpecs")
        self.img_races = QtWidgets.QLabel(self.centralwidget)
        self.img_races.setGeometry(QtCore.QRect(30, 80, 191, 31))
        self.img_races.setText("")
        self.img_races.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_races.setScaledContents(True)
        self.img_races.setObjectName("img_races")
        self.img_links = QtWidgets.QLabel(self.centralwidget)
        self.img_links.setGeometry(QtCore.QRect(460, 80, 221, 31))
        self.img_links.setText("")
        self.img_links.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_links.setScaledContents(True)
        self.img_links.setObjectName("img_links")
        self.img_specs = QtWidgets.QLabel(self.centralwidget)
        self.img_specs.setGeometry(QtCore.QRect(250, 80, 191, 31))
        self.img_specs.setText("")
        self.img_specs.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_specs.setScaledContents(True)
        self.img_specs.setObjectName("img_specs")
        self.push_update = QtWidgets.QPushButton(self.centralwidget)
        self.push_update.setGeometry(QtCore.QRect(400, 440, 131, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_update.setFont(font)
        self.push_update.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_update.setObjectName("push_update")
        self.img_background.raise_()
        self.img_links.raise_()
        self.img_specs.raise_()
        self.img_races.raise_()
        self.img_underRacesSpecs.raise_()
        self.Title.raise_()
        self.tableWidget_Races.raise_()
        self.label_Races.raise_()
        self.label_RacesSpecs.raise_()
        self.tableWidget_Specs.raise_()
        self.push_addRace.raise_()
        self.label_Specs.raise_()
        self.tableWidget_RacesSpecs.raise_()
        self.push_addSpec.raise_()
        self.push_goBack.raise_()
        self.push_addRaceSpec.raise_()
        self.push_update.raise_()
        RacesSpecsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(RacesSpecsWindow)
        QtCore.QMetaObject.connectSlotsByName(RacesSpecsWindow)

    def retranslateUi(self, RacesSpecsWindow):
        _translate = QtCore.QCoreApplication.translate
        RacesSpecsWindow.setWindowTitle(_translate("RacesSpecsWindow", "Расы и классы"))
        self.Title.setText(_translate("RacesSpecsWindow", "Расы и классы"))
        item = self.tableWidget_Races.horizontalHeaderItem(0)
        item.setText(_translate("RacesSpecsWindow", "id"))
        item = self.tableWidget_Races.horizontalHeaderItem(1)
        item.setText(_translate("RacesSpecsWindow", "Раса"))
        self.label_Races.setText(_translate("RacesSpecsWindow", "Расы"))
        self.label_RacesSpecs.setText(_translate("RacesSpecsWindow", "Связи"))
        item = self.tableWidget_Specs.horizontalHeaderItem(0)
        item.setText(_translate("RacesSpecsWindow", "id"))
        item = self.tableWidget_Specs.horizontalHeaderItem(1)
        item.setText(_translate("RacesSpecsWindow", "Класс"))
        self.push_addRace.setText(_translate("RacesSpecsWindow", "Добавить"))
        self.label_Specs.setText(_translate("RacesSpecsWindow", "Классы"))
        item = self.tableWidget_RacesSpecs.horizontalHeaderItem(0)
        item.setText(_translate("RacesSpecsWindow", "Расы"))
        item = self.tableWidget_RacesSpecs.horizontalHeaderItem(1)
        item.setText(_translate("RacesSpecsWindow", "Классы"))
        self.push_addSpec.setText(_translate("RacesSpecsWindow", "Добавить"))
        self.push_goBack.setText(_translate("RacesSpecsWindow", "Назад"))
        self.push_addRaceSpec.setText(_translate("RacesSpecsWindow", "Добавить"))
        self.push_update.setText(_translate("RacesSpecsWindow", "Обновить"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    RacesSpecsWindow = QtWidgets.QMainWindow()
    ui = Ui_RacesSpecsWindow()
    ui.setupUi(RacesSpecsWindow)
    RacesSpecsWindow.show()
    sys.exit(app.exec_())
