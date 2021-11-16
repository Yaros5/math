import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Button_Main import Ui_MainWindow
from Kram import Ui_MainWindow_1

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
# проводить інціалізацію 1
MainWindow = QtWidgets.QMainWindow()
ux = Ui_MainWindow_1()
ux.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())


# Прописуєм логіку кнопок

def bp():
    pass


def bp_2():
    pass


def bp_3():
    pass


def bp_4():
    pass


ui.pushButton.clicked.connect(bp)
ui.pushButton_2.clicked.connect(bp_2)
ui.pushButton_3.clicked.connect(bp_3)
ui.pushButton_4.clicked.connect(bp_4)

# виходим з вікна
sys.exit(app.exec_())
