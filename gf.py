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


# Прописуєм логіку
def bp():
    print("hello world")


ui.pushButton_2.clicked.connect(bp)

# виходим з вікна
sys.exit(app.exec_())
