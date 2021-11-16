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
    a[0][0] = int(ui.lineEdit.text())
    a[0][1] = int(ui.lineEdit_2.text())
    a[0][2] = int(ui.lineEdit_3.text())
    a[1][0] = int(ui.lineEdit_4.text())
    a[1][1] = int(ui.lineEdit_5.text())
    a[1][2] = int(ui.lineEdit_6.text())
    a[2][0] = int(ui.lineEdit_7.text())
    a[2][1] = int(ui.lineEdit_8.text())
    a[2][2] = int(ui.lineEdit_9.text())
    b1 = int(ui.lineEdit_10.text())
    b2 = int(ui.lineEdit_11.text())
    b3 = int(ui.lineEdit_12.text())
    d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
    d1 = b1*a[1][1]*a[2][2] + b3*a[0][1]*a[1][2] + b2*a[0][2]*a[2][1] - b3*a[1][1]*a[0][2] - b1*a[1][2]*a[2][1] - b2*a[0][1]*a[2][2]
    d2 = a[0][0]*b2*a[2][2] + b1*a[1][2]*a[2][0] + a[0][2]*a[1][0]*b3 - a[0][2]*b2*a[2][0] - a[0][0]*a[1][2]*b3 - b1*a[1][0]*a[2][2]
    d3 = a[0][0]*a[1][1]*b3 + a[0][1]*b2*a[2][0] + b1*a[1][0]*a[2][1] - b1*a[1][1]*a[2][0] - a[0][0]*b2*a[2][1] - a[0][1]*a[1][0]*b3
    if(d == 0):
        ui.label_3.setText("Determinant equals zero. No possible solution.")
    else:
        text = "X1 = " + str(round(d/d1,3)) +" ; X2 = "+str(round(d/d2,3))+" ; X3 = "+str(round(d/d3,3))
        ui.label_3.setText(text)

ui.pushButton.clicked.connect(bp)

# виходим з вікна
sys.exit(app.exec_())

