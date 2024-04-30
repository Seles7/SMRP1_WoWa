
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CharactersWindow(object):
    def setupUi(self, CharactersWindow):
        CharactersWindow.setObjectName("CharactersWindow")
        CharactersWindow.resize(700, 500)
        self.centralwidget = QtWidgets.QWidget(CharactersWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_CreateCharacter = QtWidgets.QPushButton(self.centralwidget)
        self.push_CreateCharacter.setGeometry(QtCore.QRect(20, 440, 171, 41))
        self.push_CreateCharacter.setObjectName("push_CreateCharacter")
        self.push_goBackP = QtWidgets.QPushButton(self.centralwidget)
        self.push_goBackP.setGeometry(QtCore.QRect(500, 440, 171, 41))
        self.push_goBackP.setObjectName("push_goBackP")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(200, 440, 131, 41))
        self.checkBox.setObjectName("checkBox")
        self.Title_Characters = QtWidgets.QLabel(self.centralwidget)
        self.Title_Characters.setGeometry(QtCore.QRect(30, 10, 531, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.Title_Characters.setFont(font)
        self.Title_Characters.setFocusPolicy(QtCore.Qt.NoFocus)
        self.Title_Characters.setObjectName("Title_Characters")
        self.table_Characters = QtWidgets.QTableWidget(self.centralwidget)
        self.table_Characters.setGeometry(QtCore.QRect(10, 60, 671, 371))
        self.table_Characters.setObjectName("table_Characters")
        self.table_Characters.setColumnCount(7)
        self.table_Characters.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_Characters.setHorizontalHeaderItem(6, item)
        self.table_Characters.verticalHeader().setVisible(False)
        self.table_Characters.verticalHeader().setDefaultSectionSize(30)
        self.table_Characters.verticalHeader().setMinimumSectionSize(23)
        CharactersWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CharactersWindow)
        QtCore.QMetaObject.connectSlotsByName(CharactersWindow)

    def retranslateUi(self, CharactersWindow):
        _translate = QtCore.QCoreApplication.translate
        CharactersWindow.setWindowTitle(_translate("CharactersWindow", "Персонажи"))
        self.push_CreateCharacter.setText(_translate("CharactersWindow", "Создать персонажа"))
        self.push_goBackP.setText(_translate("CharactersWindow", "Назад"))
        self.checkBox.setText(_translate("CharactersWindow", "Все персонажи"))
        self.Title_Characters.setText(_translate("CharactersWindow", "Персонажи"))
        item = self.table_Characters.horizontalHeaderItem(0)
        item.setText(_translate("CharactersWindow", "id"))
        item = self.table_Characters.horizontalHeaderItem(1)
        item.setText(_translate("CharactersWindow", "Имя"))
        item = self.table_Characters.horizontalHeaderItem(2)
        item.setText(_translate("CharactersWindow", "Раса"))
        item = self.table_Characters.horizontalHeaderItem(3)
        item.setText(_translate("CharactersWindow", "Класс"))
        item = self.table_Characters.horizontalHeaderItem(4)
        item.setText(_translate("CharactersWindow", "Уровень"))
        item = self.table_Characters.horizontalHeaderItem(5)
        item.setText(_translate("CharactersWindow", "Гильдия"))
        item = self.table_Characters.horizontalHeaderItem(6)
        item.setText(_translate("CharactersWindow", "Аккаунт"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CharactersWindow = QtWidgets.QMainWindow()
    ui = Ui_CharactersWindow()
    ui.setupUi(CharactersWindow)
    CharactersWindow.show()
    sys.exit(app.exec_())
