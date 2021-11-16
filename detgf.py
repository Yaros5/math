import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Det import Ui_MainWindow_2

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow_2()
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
    d = a[0][0]*a[1][1]*a[2][2] + a[0][1]*a[1][2]*a[2][0] + a[0][2]*a[1][0]*a[2][1] - a[0][2]*a[1][1]*a[2][0] - a[0][0]*a[1][2]*a[2][1] - a[0][1]*a[1][0]*a[2][2]
    text = "Determinant = "+ str(d)
    ui.label_3.setText(text)

ui.pushButton.clicked.connect(bp)

# виходим з вікна
sys.exit(app.exec_())


