import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Button_Main import Ui_MainWindow

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()


# Прописуєм логіку кнопок

def bp():
    MainWindow.hide()
    MainWindow = QtWidgets.QCalcDeterminant()
    ui = Ui_CalcDeterminant()
    ui.setupUi(MainWindow)
    MainWindow.show()

def bp_2():
    MainWindow.hide()
    MainWindow = QtWidgets.QCalcInverted()
    ui = Ui_CalcInverted()
    ui.setupUi(MainWindow)
    MainWindow.show()

def bp_3():
    MainWindow.hide()
    MainWindow = QtWidgets.QCalcKramar()
    ui = Ui_CalcKramar()
    ui.setupUi(MainWindow)
    MainWindow.show()

def bp_4():
    MainWindow.hide()
    MainWindow = QtWidgets.QCalcTranspont()
    ui = Ui_CalcTranspont()
    ui.setupUi(MainWindow)
    MainWindow.show()


ui.pushButton.clicked.connect(bp)
ui.pushButton_2.clicked.connect(bp_2)
ui.pushButton_3.clicked.connect(bp_3)
ui.pushButton_4.clicked.connect(bp_4)

# виходим з вікна
sys.exit(app.exec_())
