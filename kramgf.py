import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Kram import Ui_MainWindow_1

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow_1()
ui.setupUi(MainWindow)
MainWindow.show()


# Прописуєм логіку кнопки

def bp():
    a = [[0,0,0],[0,0,0],[0,0,0]]
    a[0][0] = ui.spinBox.value()
    a[0][1] = ui.spinBox_1.value()
    a[0][2] = ui.spinBox_2.value()
    a[1][0] = ui.spinBox_3.value()
    a[1][1] = ui.spinBox_4.value()
    a[1][2] = ui.spinBox_5.value()
    a[2][0] = ui.spinBox_6.value()
    a[2][1] = ui.spinBox_7.value()
    a[2][2] = ui.spinBox_8.value()
    d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
	print(d)
    pass

ui.pushButton.clicked.connect(bp)

# виходим з вікна
sys.exit(app.exec_())

