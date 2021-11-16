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
# лінійні рівняння
def lin():
    a = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    a[0][0] = int(ux.lineEdit.text())
    a[0][1] = int(ux.lineEdit_2.text())
    a[0][2] = int(ux.lineEdit_3.text())
    a[1][0] = int(ux.lineEdit_4.text())
    a[1][1] = int(ux.lineEdit_5.text())
    a[1][2] = int(ux.lineEdit_6.text())
    a[2][0] = int(ux.lineEdit_7.text())
    a[2][1] = int(ux.lineEdit_8.text())
    a[2][2] = int(ux.lineEdit_9.text())
    b1 = int(ux.lineEdit_10.text())
    b2 = int(ux.lineEdit_11.text())
    b3 = int(ux.lineEdit_12.text())
    d = a[0][0] * a[1][1] * a[2][2] + a[0][1] * a[1][2] * a[2][0] + a[0][2] * a[1][0] * a[2][1] - a[0][2] * a[1][
        1] * \
        a[2][0] - a[0][0] * a[1][2] * a[2][1] - a[0][1] * a[1][0] * a[2][2]
    d1 = b1 * a[1][1] * a[2][2] + b3 * a[0][1] * a[1][2] + b2 * a[0][2] * a[2][1] - b3 * a[1][1] * a[0][2] - b1 * \
         a[1][
             2] * a[2][1] - b2 * a[0][1] * a[2][2]
    d2 = a[0][0] * b2 * a[2][2] + b1 * a[1][2] * a[2][0] + a[0][2] * a[1][0] * b3 - a[0][2] * b2 * a[2][0] - a[0][
        0] * \
         a[1][2] * b3 - b1 * a[1][0] * a[2][2]
    d3 = a[0][0] * a[1][1] * b3 + a[0][1] * b2 * a[2][0] + b1 * a[1][0] * a[2][1] - b1 * a[1][1] * a[2][0] - a[0][
        0] * b2 * a[2][1] - a[0][1] * a[1][0] * b3
    if (d == 0):
        ux.label_3.setText("Determinant equals zero. No possible solution.")
    else:
        text = "X1 = " + str(round(d / d1, 3)) + " ; X2 = " + str(round(d / d2, 3)) + " ; X3 = " + str(
            round(d / d3, 3))
        ux.label_3.setText(text)
#обернена матриця
def ober():
    a = [[0,0,0],[0,0,0],[0,0,0]]
    A = [[0,0,0],[0,0,0],[0,0,0]]
    a[0][0] = int(x.lineEdit.text())
    a[0][1] = int(x.lineEdit_2.text())
    a[0][2] = int(x.lineEdit_3.text())
    a[1][0] = int(x.lineEdit_4.text())
    a[1][1] = int(x.lineEdit_5.text())
    a[1][2] = int(x.lineEdit_6.text())
    a[2][0] = int(x.lineEdit_7.text())
    a[2][1] = int(x.lineEdit_8.text())
    a[2][2] = int(x.lineEdit_9.text())
    d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
    if(d == 0):
        x.label_3.setText("Determinant equals zero. No inverted matrix possible.")
    else:
        x.label_3.setText(str(round((a[1][1] * a[2][2] - a[1][2] * a[2][1])/d,3)))
        x.label_6.setText(str(round(-1 * (a[1][0] * a[2][2] - a[1][2] * a[2][0])/d,3)))
        x.label_9.setText(str(round((a[1][0] * a[2][1] - a[1][1] * a[2][0])/d,3)))
        x.label_4.setText(str(round(-1 * (a[0][1] * a[2][2] - a[0][2] * a[2][1])/d,3)))
        x.label_7.setText(str(round((a[0][0] * a[2][2] - a[0][2] * a[2][0])/d,3)))
        x.label_10.setText(str(round(-1 * (a[0][0] * a[2][1] - a[0][1] * a[2][0])/d,3)))
        x.label_5.setText(str(round((a[0][1] * a[1][2] - a[0][2] * a[1][1])/d,3)))
        x.label_8.setText(str(round(-1 * (a[0][0] * a[1][2] - a[0][2] * a[1][0])/d,3)))
        x.label_11.setText(str(round((a[0][0] * a[1][1] - a[0][1] * a[1][0])/d,3)))
# визначник
def det():
    a = [[0,0,0],[0,0,0],[0,0,0]]
    a[0][0] = int(uix.lineEdit.text())
    a[0][1] = int(uix.lineEdit_2.text())
    a[0][2] = int(uix.lineEdit_3.text())
    a[1][0] = int(uix.lineEdit_4.text())
    a[1][1] = int(uix.lineEdit_5.text())
    a[1][2] = int(uix.lineEdit_6.text())
    a[2][0] = int(uix.lineEdit_7.text())
    a[2][1] = int(uix.lineEdit_8.text())
    a[2][2] = int(uix.lineEdit_9.text())
    d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
    text = "Determinant = "+ str(d)
    uix.label_3.setText(text)

#транспортування матриця
def trans():
    uixi.label_3.setText(uixi.lineEdit.text())
    uixi.label_6.setText(uixi.lineEdit_2.text())
    uixi.label_9.setText(uixi.lineEdit_3.text())
    uixi.label_4.setText(uixi.lineEdit_4.text())
    uixi.label_7.setText(uixi.lineEdit_5.text())
    uixi.label_10.setText(uixi.lineEdit_6.text())
    uixi.label_5.setText(uixi.lineEdit_7.text())
    uixi.label_8.setText(uixi.lineEdit_8.text())
    uixi.label_11.setText(uixi.lineEdit_9.text())
#детермінант
def bp():
    MainW.show()
    uix.pushButton.clicked.connect(det)

#обернена матриця
def bp_2():
    MainWin.show()
    x.pushButton.clicked.connect(ober)
#лінійні рівнняня
def bp_3():
    Main.show()
    ux.pushButton.clicked.connect(lin)
#транспортування матриці

def bp_4():
    MainWi.show()
    uixi.pushButton.clicked.connect(trans)

ui.pushButton.clicked.connect(bp)
ui.pushButton_2.clicked.connect(bp_2)
ui.pushButton_3.clicked.connect(bp_3)
ui.pushButton_4.clicked.connect(bp_4)

# виходим з вікна
sys.exit(app.exec_())
