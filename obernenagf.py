import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Reversed import Ui_MainWindow_4

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow_4()
ui.setupUi(MainWindow)
MainWindow.show()


# Прописуєм логіку кнопки

def bp():
    a = [[0,0,0],[0,0,0],[0,0,0]]
    A = [[0,0,0],[0,0,0],[0,0,0]]
    a[0][0] = int(ui.lineEdit.text())
    a[0][1] = int(ui.lineEdit_2.text())
    a[0][2] = int(ui.lineEdit_3.text())
    a[1][0] = int(ui.lineEdit_4.text())
    a[1][1] = int(ui.lineEdit_5.text())
    a[1][2] = int(ui.lineEdit_6.text())
    a[2][0] = int(ui.lineEdit_7.text())
    a[2][1] = int(ui.lineEdit_8.text())
    a[2][2] = int(ui.lineEdit_9.text())
    d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
    if(d == 0):
        ui.label_3.setText("Determinant equals zero. No inverted matrix possible.")
    else:
        ui.label_3.setText(str(round((a[1][1] * a[2][2] - a[1][2] * a[2][1])/d,3))) 
        ui.label_6.setText(str(round(-1 * (a[1][0] * a[2][2] - a[1][2] * a[2][0])/d,3)))  
        ui.label_9.setText(str(round((a[1][0] * a[2][1] - a[1][1] * a[2][0])/d,3))) 
        ui.label_4.setText(str(round(-1 * (a[0][1] * a[2][2] - a[0][2] * a[2][1])/d,3))) 
        ui.label_7.setText(str(round((a[0][0] * a[2][2] - a[0][2] * a[2][0])/d,3))) 
        ui.label_10.setText(str(round(-1 * (a[0][0] * a[2][1] - a[0][1] * a[2][0])/d,3))) 
        ui.label_5.setText(str(round((a[0][1] * a[1][2] - a[0][2] * a[1][1])/d,3)))  
        ui.label_8.setText(str(round(-1 * (a[0][0] * a[1][2] - a[0][2] * a[1][0])/d,3)))  
        ui.label_11.setText(str(round((a[0][0] * a[1][1] - a[0][1] * a[1][0])/d,3))) 

ui.pushButton.clicked.connect(bp)

# виходим з вікна
sys.exit(app.exec_())

