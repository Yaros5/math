from target import Main
from PyQt5 import QtCore, QtGui, QtWidgets
from  graph import *
import sys

app = QtWidgets.QApplication(sys.argv)

MainWindow = QtWidgets.QMainWindow()
ui = Main()
ui.setupUi(MainWindow)
MainWindow.show()


def bp():
    pass
ui.pushButton_2.clicked.connect(bp)

sys.exit(app.exec_())
