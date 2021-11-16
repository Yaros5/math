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


def bp_2():


def bp_3():


def bp_4():



ui.pushButton.clicked.connect(bp)
ui.pushButton_2.clicked.connect(bp_2)
ui.pushButton_3.clicked.connect(bp_3)
ui.pushButton_4.clicked.connect(bp_4)

# виходим з вікна
sys.exit(app.exec_())
