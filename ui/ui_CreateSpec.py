# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\CreateClass_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CreateSpecWidget(object):
    def setupUi(self, CreateSpecWidget):
        CreateSpecWidget.setObjectName("CreateSpecWidget")
        CreateSpecWidget.resize(400, 250)
        CreateSpecWidget.setMinimumSize(QtCore.QSize(400, 250))
        CreateSpecWidget.setMaximumSize(QtCore.QSize(400, 250))
        self.push_AceptCreate = QtWidgets.QPushButton(CreateSpecWidget)
        self.push_AceptCreate.setGeometry(QtCore.QRect(10, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_AceptCreate.setFont(font)
        self.push_AceptCreate.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_AceptCreate.setObjectName("push_AceptCreate")
        self.push_GoBack = QtWidgets.QPushButton(CreateSpecWidget)
        self.push_GoBack.setGeometry(QtCore.QRect(240, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_GoBack.setFont(font)
        self.push_GoBack.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_GoBack.setObjectName("push_GoBack")
        self.formLayoutWidget = QtWidgets.QWidget(CreateSpecWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 100, 291, 41))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label_Name = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.label_Name.setFont(font)
        self.label_Name.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 253, 189)")
        self.label_Name.setObjectName("label_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_Name)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Name)
        self.label_Spec = QtWidgets.QLabel(CreateSpecWidget)
        self.label_Spec.setGeometry(QtCore.QRect(110, 10, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        self.label_Spec.setFont(font)
        self.label_Spec.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_Spec.setObjectName("label_Spec")
        self.img_underSpec = QtWidgets.QLabel(CreateSpecWidget)
        self.img_underSpec.setGeometry(QtCore.QRect(60, 10, 281, 41))
        self.img_underSpec.setStyleSheet("background-image: url(:/newPrefix/Downloads/kisspng-paper-scroll-parchment-clip-art-landscape-apge-with-pen-5b0bcdc6e5bf67.4688394015275002309411.png);")
        self.img_underSpec.setText("")
        self.img_underSpec.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underSpec.setScaledContents(True)
        self.img_underSpec.setObjectName("img_underSpec")
        self.img_background = QtWidgets.QLabel(CreateSpecWidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.img_background.setMinimumSize(QtCore.QSize(400, 250))
        self.img_background.setMaximumSize(QtCore.QSize(400, 250))
        self.img_background.setStyleSheet("background-image: url(:/newPrefix/Desktop/Прочее/ca2c1866ea4cc5d07e622ab207ddc622.jpg);")
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/heroes.jpg"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.img_background.raise_()
        self.img_underSpec.raise_()
        self.push_AceptCreate.raise_()
        self.push_GoBack.raise_()
        self.formLayoutWidget.raise_()
        self.label_Spec.raise_()

        self.retranslateUi(CreateSpecWidget)
        QtCore.QMetaObject.connectSlotsByName(CreateSpecWidget)

    def retranslateUi(self, CreateSpecWidget):
        _translate = QtCore.QCoreApplication.translate
        CreateSpecWidget.setWindowTitle(_translate("CreateSpecWidget", "Создание класса"))
        self.push_AceptCreate.setText(_translate("CreateSpecWidget", "Создать"))
        self.push_GoBack.setText(_translate("CreateSpecWidget", "Отмена"))
        self.label_Name.setText(_translate("CreateSpecWidget", "Название"))
        self.label_Spec.setText(_translate("CreateSpecWidget", "Создание класса"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateSpecWidget = QtWidgets.QWidget()
    ui = Ui_CreateSpecWidget()
    ui.setupUi(CreateSpecWidget)
    CreateSpecWidget.show()
    sys.exit(app.exec_())
