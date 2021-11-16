import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Reversed import Ui_MainWindow_3

# додаєм в проект стартовий файл
app = QtWidgets.QApplication(sys.argv)

# проводим ініціалізації
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow_3()
ui.setupUi(MainWindow)
MainWindow.show()


# Прописуєм логіку кнопки

def bp():
    ui.label_3.setText(ui.lineEdit.text())
    ui.label_6.setText(ui.lineEdit_2.text())  
    ui.label_9.setText(ui.lineEdit_3.text()) 
    ui.label_4.setText(ui.lineEdit_4.text()) 
    ui.label_7.setText(ui.lineEdit_5.text()) 
    ui.label_10.setText(ui.lineEdit_6.text()) 
    ui.label_5.setText(ui.lineEdit_7.text())  
    ui.label_8.setText(ui.lineEdit_8.text())  
    ui.label_11.setText(ui.lineEdit_9.text()) 

ui.pushButton.clicked.connect(bp)

# виходим з вікна
sys.exit(app.exec_())

