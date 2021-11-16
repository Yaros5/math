import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Button_Main import Ui_MainWindow
from Kram import Ui_MainWindow_1
from Det import Ui_MainWindow_2
from Trans import Ui_MainWindow_3
from Reversed import Ui_MainWindow_4

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()

# проводить інціалізацію 1
Main = QtWidgets.QMainWindow()
ux = Ui_MainWindow_1()
ux.setupUi(Main)
# проводить інціалізацію 2

MainW = QtWidgets.QMainWindow()
uix = Ui_MainWindow_2()
uix.setupUi(MainW)
# проводить інціалізацію 3

MainWi = QtWidgets.QMainWindow()
uixi = Ui_MainWindow_3()
uixi.setupUi(MainWi)

MainWin = QtWidgets.QMainWindow()
x = Ui_MainWindow_4()
x.setupUi(MainWin)


# Прописуєм логіку кнопок

def bp():
    MainW.show()


def bp_2():
    MainWi.show()


def bp_3():
    Main.show()


def bp_4():
    MainWin.show()


ui.pushButton.clicked.connect(bp)
ui.pushButton_2.clicked.connect(bp_2)
ui.pushButton_3.clicked.connect(bp_3)
ui.pushButton_4.clicked.connect(bp_4)

# виходим з вікна
sys.exit(app.exec_())
