# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\CreateGuild_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateGuildWidget(object):
    def setupUi(self, CreateGuildWidget):
        CreateGuildWidget.setObjectName("CreateGuildWidget")
        CreateGuildWidget.resize(400, 250)
        CreateGuildWidget.setMinimumSize(QtCore.QSize(400, 250))
        CreateGuildWidget.setMaximumSize(QtCore.QSize(400, 250))
        self.push_CreateGuild = QtWidgets.QPushButton(CreateGuildWidget)
        self.push_CreateGuild.setGeometry(QtCore.QRect(10, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_CreateGuild.setFont(font)
        self.push_CreateGuild.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_CreateGuild.setObjectName("push_CreateGuild")
        self.push_GoBack = QtWidgets.QPushButton(CreateGuildWidget)
        self.push_GoBack.setGeometry(QtCore.QRect(240, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        font.setItalic(False)
        self.push_GoBack.setFont(font)
        self.push_GoBack.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_GoBack.setObjectName("push_GoBack")
        self.title = QtWidgets.QLabel(CreateGuildWidget)
        self.title.setGeometry(QtCore.QRect(100, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.title.setObjectName("title")
        self.img_title = QtWidgets.QLabel(CreateGuildWidget)
        self.img_title.setGeometry(QtCore.QRect(60, 10, 281, 41))
        self.img_title.setStyleSheet("")
        self.img_title.setText("")
        self.img_title.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_title.setScaledContents(True)
        self.img_title.setObjectName("img_title")
        self.img_background = QtWidgets.QLabel(CreateGuildWidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.img_background.setStyleSheet("background-image: url(:/newPrefix/Desktop/Прочее/Vorota.png);")
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/guilds.jpg"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.formLayoutWidget = QtWidgets.QWidget(CreateGuildWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 80, 301, 91))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.comboBox_character = QtWidgets.QComboBox(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.comboBox_character.setFont(font)
        self.comboBox_character.setObjectName("comboBox_character")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboBox_character)
        self.TitleGuild = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.TitleGuild.setFont(font)
        self.TitleGuild.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.TitleGuild.setObjectName("TitleGuild")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.TitleGuild)
        self.LineEdit_TitleGuild = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.LineEdit_TitleGuild.setFont(font)
        self.LineEdit_TitleGuild.setObjectName("LineEdit_TitleGuild")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.LineEdit_TitleGuild)
        self.TitleCharacter = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.TitleCharacter.setFont(font)
        self.TitleCharacter.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.TitleCharacter.setObjectName("TitleCharacter")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.TitleCharacter)
        self.img_background.raise_()
        self.img_title.raise_()
        self.push_CreateGuild.raise_()
        self.push_GoBack.raise_()
        self.title.raise_()
        self.formLayoutWidget.raise_()

        self.retranslateUi(CreateGuildWidget)
        QtCore.QMetaObject.connectSlotsByName(CreateGuildWidget)

    def retranslateUi(self, CreateGuildWidget):
        _translate = QtCore.QCoreApplication.translate
        CreateGuildWidget.setWindowTitle(_translate("CreateGuildWidget", "Создание гильдии"))
        self.push_CreateGuild.setText(_translate("CreateGuildWidget", "Основать Гильдию"))
        self.push_GoBack.setText(_translate("CreateGuildWidget", "Отмена"))
        self.title.setText(_translate("CreateGuildWidget", "Создание Гильдии"))
        self.TitleGuild.setText(_translate("CreateGuildWidget", "Название    "))
        self.TitleCharacter.setText(_translate("CreateGuildWidget", "Основатель"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateGuildWidget = QtWidgets.QWidget()
    ui = Ui_CreateGuildWidget()
    ui.setupUi(CreateGuildWidget)
    CreateGuildWidget.show()
    sys.exit(app.exec_())
