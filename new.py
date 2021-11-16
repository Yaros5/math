import sys
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_MainWindow_3(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 515)
        MainWindow.setStyleSheet("background: #34495e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 81, 17))
        self.label.setStyleSheet("color: #fff\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 410, 131, 41))
        self.pushButton.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 200px;\n"
"  height: 100px;\n"
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 130, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 210, 231, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 290, 231, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_7.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_9.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 90, 81, 17))
        self.label_2.setStyleSheet("color: #fff\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 130, 231, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("color: #fff\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("color: #fff\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color: #fff\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("color: #fff\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color: #fff\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color: #fff\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("color: #fff\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("color: #fff\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("color: #fff\n"
"")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Транспонування матриці"))
        self.label.setText(_translate("MainWindow", "Матриця A"))
        self.pushButton.setText(_translate("MainWindow", "Обчислити"))
        self.label_2.setText(_translate("MainWindow", "Відповідь:"))

class Ui_MainWindow_4(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 515)
        MainWindow.setStyleSheet("background: #34495e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 81, 17))
        self.label.setStyleSheet("color: #fff\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(230, 410, 131, 41))
        self.pushButton.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 200px;\n"
"  height: 100px;\n"
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 130, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 210, 231, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 290, 231, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_7.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_9.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(400, 90, 81, 17))
        self.label_2.setStyleSheet("color: #fff\n"
"")
        self.label_2.setObjectName("label_2")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(320, 130, 231, 241))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_8.setStyleSheet("color: #fff\n"
"")
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 2, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_7.setStyleSheet("color: #fff\n"
"")
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_4.setStyleSheet("color: #fff\n"
"")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_6.setStyleSheet("color: #fff\n"
"")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_3.setStyleSheet("color: #fff\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_5.setStyleSheet("color: #fff\n"
"")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 2, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_9.setStyleSheet("color: #fff\n"
"")
        self.label_9.setText("")
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 2, 0, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_10.setStyleSheet("color: #fff\n"
"")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_11.setStyleSheet("color: #fff\n"
"")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Обернена матриця"))
        self.label.setText(_translate("MainWindow", "Матриця A"))
        self.pushButton.setText(_translate("MainWindow", "Обчислити"))
        self.label_2.setText(_translate("MainWindow", "Відповідь:"))


class Ui_MainWindow_2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 502)
        MainWindow.setStyleSheet("background: #34495e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 60, 81, 17))
        self.label.setStyleSheet("color: #fff\n"
"")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 350, 131, 41))
        self.pushButton.setStyleSheet(".QPushButton {\n"
"  border: none;\n"
"  background: #ecf0f1;\n"
"  color: #000;\n"
"  border-radius: 20px;\n"
"  width: 200px;\n"
"  height: 100px;\n"
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 90, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 170, 231, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 250, 231, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_7.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
                                      
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_9.setStyleSheet(".QLineEdit {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QLineEdit:hover {\n"
"  background: #2c3e50;\n"
"}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 440, 181, 17))
        self.label_3.setStyleSheet("color: #fff\n"
"")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Визначник матриці"))
        self.label.setText(_translate("MainWindow", "Матриця A"))
        self.pushButton.setText(_translate("MainWindow", "Обчислити"))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Меню"))
        self.pushButton_2.setText(_translate("MainWindow", "Обернена матриця"))
        self.pushButton_3.setText(_translate("MainWindow", "Лінійне рівняння"))
        self.pushButton_4.setText(_translate("MainWindow", "Транспонування"))
        self.pushButton.setText(_translate("MainWindow", "Визначник матриці"))


class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(477, 515)
        MainWindow.setStyleSheet("background: #34495e")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 80, 81, 17))
        self.label.setStyleSheet("color: #fff\n"
                                 "")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(320, 80, 81, 20))
        self.label_2.setStyleSheet("color: #fff\n"
                                   "")
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 410, 131, 41))
        self.pushButton.setStyleSheet(".QPushButton {\n"
                                      "  border: none;\n"
                                      "  background: #ecf0f1;\n"
                                      "  color: #000;\n"
                                      "  border-radius: 20px;\n"
                                      "  width: 200px;\n"
                                      "  height: 100px;\n"
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 130, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit.setStyleSheet(".QLineEdit {\n"
                                    "  color: #fff;\n"
                                    "  font-size: 15px;\n"
                                    "}\n"
                                    "\n"
                                    ".QLineEdit:hover {\n"
                                    "  background: #2c3e50;\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_2.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout.addWidget(self.lineEdit_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 210, 231, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.horizontalLayout_2.addWidget(self.lineEdit_4)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_5.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_2.addWidget(self.lineEdit_5)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_6.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_2.addWidget(self.lineEdit_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 290, 231, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_7.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_3.addWidget(self.lineEdit_7)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_8.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_3.addWidget(self.lineEdit_8)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_9.setStyleSheet(".QLineEdit {\n"
                                      "  color: #fff;\n"
                                      "  font-size: 15px;\n"
                                      "}\n"
                                      "\n"
                                      ".QLineEdit:hover {\n"
                                      "  background: #2c3e50;\n"
                                      "}")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.horizontalLayout_3.addWidget(self.lineEdit_9)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 110, 81, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_10.setStyleSheet(".QLineEdit {\n"
                                       "  color: #fff;\n"
                                       "  font-size: 15px;\n"
                                       "}\n"
                                       "\n"
                                       ".QLineEdit:hover {\n"
                                       "  background: #2c3e50;\n"
                                       "}")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.verticalLayout.addWidget(self.lineEdit_10)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_11.setStyleSheet(".QLineEdit {\n"
                                       "  color: #fff;\n"
                                       "  font-size: 15px;\n"
                                       "}\n"
                                       "\n"
                                       ".QLineEdit:hover {\n"
                                       "  background: #2c3e50;\n"
                                       "}")
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.verticalLayout.addWidget(self.lineEdit_11)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_12.setStyleSheet(".QLineEdit {\n"
                                       "  color: #fff;\n"
                                       "  font-size: 15px;\n"
                                       "}\n"
                                       "\n"
                                       ".QLineEdit:hover {\n"
                                       "  background: #2c3e50;\n"
                                       "}")
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.verticalLayout.addWidget(self.lineEdit_12)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 420, 181, 17))
        self.label_3.setStyleSheet("color: #fff;\n""font-size: 12px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Лінійне рівняння"))
        self.label.setText(_translate("MainWindow", "Матриця A"))
        self.label_2.setText(_translate("MainWindow", "Матриця B"))
        self.pushButton.setText(_translate("MainWindow", "Обчислити"))




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
        ux.label_3.setText("Determinant equals zero")
    else:
        text = "X1 = " + str(round(d / d1, 1)) + "; X2 = " + str(round(d / d2, 1)) + "; X3 = " + str(
            round(d / d3, 1))
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
