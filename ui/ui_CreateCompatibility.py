# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\from_designer\CreateCompatibility_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CompatibilityWidget(object):
    def setupUi(self, CompatibilityWidget):
        CompatibilityWidget.setObjectName("CompatibilityWidget")
        CompatibilityWidget.resize(400, 250)
        CompatibilityWidget.setMinimumSize(QtCore.QSize(400, 250))
        CompatibilityWidget.setMaximumSize(QtCore.QSize(400, 250))
        font = QtGui.QFont()
        font.setPointSize(8)
        CompatibilityWidget.setFont(font)
        self.push_AceptCreate = QtWidgets.QPushButton(CompatibilityWidget)
        self.push_AceptCreate.setGeometry(QtCore.QRect(10, 200, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_AceptCreate.setFont(font)
        self.push_AceptCreate.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_AceptCreate.setObjectName("push_AceptCreate")
        self.push_GoBack = QtWidgets.QPushButton(CompatibilityWidget)
        self.push_GoBack.setGeometry(QtCore.QRect(240, 200, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.push_GoBack.setFont(font)
        self.push_GoBack.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0.0340909, stop:0 rgba(61, 61, 61, 255), stop:1 rgba(124, 124, 124, 255));\n"
"color: rgb(255, 253, 189)")
        self.push_GoBack.setObjectName("push_GoBack")
        self.formLayoutWidget = QtWidgets.QWidget(CompatibilityWidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 80, 291, 81))
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
        self.label_Password = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(18)
        self.label_Password.setFont(font)
        self.label_Password.setStyleSheet("background-color: rgb(61, 61, 61);\n"
"color: rgb(255, 253, 189)")
        self.label_Password.setObjectName("label_Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_Password)
        self.lineEdit_Password = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_Password.setFont(font)
        self.lineEdit_Password.setObjectName("lineEdit_Password")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Password)
        self.lineEdit_Name = QtWidgets.QLineEdit(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit_Name.setFont(font)
        self.lineEdit_Name.setObjectName("lineEdit_Name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_Name)
        self.label_Compatibility = QtWidgets.QLabel(CompatibilityWidget)
        self.label_Compatibility.setGeometry(QtCore.QRect(100, 10, 181, 31))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(22)
        self.label_Compatibility.setFont(font)
        self.label_Compatibility.setStyleSheet("color: rgb(0, 0, 0);\n"
"\n"
"")
        self.label_Compatibility.setObjectName("label_Compatibility")
        self.img_underCompat = QtWidgets.QLabel(CompatibilityWidget)
        self.img_underCompat.setGeometry(QtCore.QRect(60, 10, 261, 41))
        self.img_underCompat.setStyleSheet("background-image: url(:/newPrefix/Downloads/kisspng-paper-scroll-parchment-clip-art-landscape-apge-with-pen-5b0bcdc6e5bf67.4688394015275002309411.png);")
        self.img_underCompat.setText("")
        self.img_underCompat.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underCompat.setScaledContents(True)
        self.img_underCompat.setObjectName("img_underCompat")
        self.img_background = QtWidgets.QLabel(CompatibilityWidget)
        self.img_background.setGeometry(QtCore.QRect(0, 0, 400, 250))
        self.img_background.setMinimumSize(QtCore.QSize(400, 250))
        self.img_background.setMaximumSize(QtCore.QSize(400, 250))
        self.img_background.setStyleSheet("background-image: url(:/newPrefix/Desktop/Прочее/uj7jKpEfRT4.jpg);")
        self.img_background.setText("")
        self.img_background.setPixmap(QtGui.QPixmap(":/pins1/heroes.jpg"))
        self.img_background.setScaledContents(True)
        self.img_background.setObjectName("img_background")
        self.labe_warning = QtWidgets.QLabel(CompatibilityWidget)
        self.labe_warning.setGeometry(QtCore.QRect(80, 170, 241, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.labe_warning.setFont(font)
        self.labe_warning.setStyleSheet("color: rgb(147, 0, 0);")
        self.labe_warning.setObjectName("labe_warning")
        self.img_underWarning = QtWidgets.QLabel(CompatibilityWidget)
        self.img_underWarning.setGeometry(QtCore.QRect(30, 170, 341, 21))
        self.img_underWarning.setStyleSheet("background-image: url(:/newPrefix/Downloads/kisspng-paper-scroll-parchment-clip-art-landscape-apge-with-pen-5b0bcdc6e5bf67.4688394015275002309411.png);")
        self.img_underWarning.setText("")
        self.img_underWarning.setPixmap(QtGui.QPixmap(":/pins1/pergament2.png"))
        self.img_underWarning.setScaledContents(True)
        self.img_underWarning.setObjectName("img_underWarning")
        self.img_background.raise_()
        self.img_underWarning.raise_()
        self.img_underCompat.raise_()
        self.push_AceptCreate.raise_()
        self.push_GoBack.raise_()
        self.formLayoutWidget.raise_()
        self.label_Compatibility.raise_()
        self.labe_warning.raise_()

        self.retranslateUi(CompatibilityWidget)
        QtCore.QMetaObject.connectSlotsByName(CompatibilityWidget)

    def retranslateUi(self, CompatibilityWidget):
        _translate = QtCore.QCoreApplication.translate
        CompatibilityWidget.setWindowTitle(_translate("CompatibilityWidget", "Создание связи расы и класса"))
        self.push_AceptCreate.setText(_translate("CompatibilityWidget", "Создать"))
        self.push_GoBack.setText(_translate("CompatibilityWidget", "Отмена"))
        self.label_Name.setText(_translate("CompatibilityWidget", " Раса "))
        self.label_Password.setText(_translate("CompatibilityWidget", "Класс"))
        self.label_Compatibility.setText(_translate("CompatibilityWidget", "Совместимость"))
        self.labe_warning.setText(_translate("CompatibilityWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:8pt;\">Писать Расы и Классы идентично табличным!</span></p></body></html>"))
import images.resource1_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CompatibilityWidget = QtWidgets.QWidget()
    ui = Ui_CompatibilityWidget()
    ui.setupUi(CompatibilityWidget)
    CompatibilityWidget.show()
    sys.exit(app.exec_())
