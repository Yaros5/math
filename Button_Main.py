# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Button_Main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(527, 255)
        MainWindow.setStyleSheet("background: #34495e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(50, 30, 421, 181))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 100px;\n"
"  height: 50px;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #bdc3c7;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"  width: 95px;\n"
"  height: 18px;\n"
"  font-size: 14px;\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 100px;\n"
"  height: 50px;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #bdc3c7;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"  width: 95px;\n"
"  height: 18px;\n"
"  font-size: 14px;\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 100px;\n"
"  height: 50px;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #bdc3c7;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"  width: 95px;\n"
"  height: 18px;\n"
"  font-size: 14px;\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 100px;\n"
"  height: 50px;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QPushButton:hover {\n"
"  background: #bdc3c7;\n"
"}\n"
"\n"
".QPushButton:pressed {\n"
"  width: 95px;\n"
"  height: 18px;\n"
"  font-size: 14px;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "Обернена матриця"))
        self.pushButton_3.setText(_translate("MainWindow", "Лінійне рівняння"))
        self.pushButton_4.setText(_translate("MainWindow", "Транспонування"))
        self.pushButton.setText(_translate("MainWindow", "Визначник"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
