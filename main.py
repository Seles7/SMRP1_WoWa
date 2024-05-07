import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication

from windows import entrance_window

sys._excepthook = sys.excepthook


def exception_hook(exctype, value, traceback):
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)


sys.excepthook = exception_hook

app = QApplication(sys.argv)


entrance = entrance_window.Entrance()
entrance.show()


sys.exit(app.exec_())