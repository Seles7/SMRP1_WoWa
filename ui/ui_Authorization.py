# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\Authorization_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AuthorizationWidget(object):
    def setupUi(self, AuthorizationWidget):
        AuthorizationWidget.setObjectName("AuthorizationWidget")
        AuthorizationWidget.resize(400, 250)
        AuthorizationWidget.setMinimumSize(QtCore.QSize(400, 250))
        AuthorizationWidget.setMaximumSize(QtCore.QSize(400, 250))
        self.push_AceptAuthoriz = QtWidgets.QPushButton(AuthorizationWidget)
        self.push_AceptAuthoriz.setGeometry(QtCore.QRect(10, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_AceptAuthoriz.setFont(font)
        self.push_AceptAuthoriz.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_AceptAuthoriz.setObjectName("push_AceptAuthoriz")
        self.push_GoBack = QtWidgets.QPushButton(AuthorizationWidget)
        self.push_GoBack.setGeometry(QtCore.QRect(240, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(16)
        self.push_GoBack.setFont(font)
        self.push_GoBack.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_GoBack.setObjectName("push_GoBack")
        self.formLayoutWidget = QtWidgets.QWidget(AuthorizationWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 90, 291, 77))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_Name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.label_Name.setFont(font)
        self.label_Name.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 253, 189)")
        self.label_Name.setObjectName("label_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Name)
        self.label_Password = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(14)
        self.label_Password.setFont(font)
        self.label_Password.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 253, 189)")
        self.label_Password.setObjectName("label_Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Password)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Name)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Password)
        self.label_Authorization = QtWidgets.QLabel(AuthorizationWidget)
        self.label_Authorization.setGeometry(QtCore.QRect(120, 10, 151, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        self.label_Authorization.setFont(font)
        self.label_Authorization.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_Authorization.setObjectName("label_Authorization")
        self.img_underAuthoriz = QtWidgets.QLabel(AuthorizationWidget)
        self.img_underAuthoriz.setGeometry(QtCore.QRect(90, 10, 211, 41))
        self.img_underAuthoriz.setStyleSheet("background-image: url(:/newPrefix/Downloads/kisspng-paper-scroll-parchment-clip-art-landscape-apge-with-pen-5b0bcdc6e5bf67.4688394015275002309411.png);")
        self.img_underAuthoriz.setText("")
        self.img_underAuthoriz.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underAuthoriz.setScaledContents(True)
        self.img_underAuthoriz.setObjectName("img_underAuthoriz")
        self.img_background = QtWidgets.QLabel(AuthorizationWidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.img_background.setStyleSheet("background-image: url(:/newPrefix/Desktop/Прочее/Vorota.png);")
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/VOROTA1.jpg"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.img_background.raise_()
        self.img_underAuthoriz.raise_()
        self.push_AceptAuthoriz.raise_()
        self.push_GoBack.raise_()
        self.formLayoutWidget.raise_()
        self.label_Authorization.raise_()

        self.retranslateUi(AuthorizationWidget)
        QtCore.QMetaObject.connectSlotsByName(AuthorizationWidget)

    def retranslateUi(self, AuthorizationWidget):
        _translate = QtCore.QCoreApplication.translate
        AuthorizationWidget.setWindowTitle(_translate("AuthorizationWidget", "Авторизация"))
        self.push_AceptAuthoriz.setText(_translate("AuthorizationWidget", "Вперёд, войти!!"))
        self.push_GoBack.setText(_translate("AuthorizationWidget", "Я передумал..."))
        self.label_Name.setText(_translate("AuthorizationWidget", "Логин  "))
        self.label_Password.setText(_translate("AuthorizationWidget", "Пароль"))
        self.label_Authorization.setText(_translate("AuthorizationWidget", "Авторизация"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AuthorizationWidget = QtWidgets.QWidget()
    ui = Ui_AuthorizationWidget()
    ui.setupUi(AuthorizationWidget)
    AuthorizationWidget.show()
    sys.exit(app.exec_())
