# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kram.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


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
        self.spinBox = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.spinBox_2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_2.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_2.setObjectName("spinBox_2")
        self.horizontalLayout.addWidget(self.spinBox_2)
        self.spinBox_3 = QtWidgets.QSpinBox(self.horizontalLayoutWidget)
        self.spinBox_3.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout.addWidget(self.spinBox_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 210, 231, 80))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinBox_4 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_4.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_2.addWidget(self.spinBox_4)
        self.spinBox_5 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_5.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_5.setObjectName("spinBox_5")
        self.horizontalLayout_2.addWidget(self.spinBox_5)
        self.spinBox_6 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        self.spinBox_6.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_6.setObjectName("spinBox_6")
        self.horizontalLayout_2.addWidget(self.spinBox_6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(40, 290, 231, 80))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinBox_7 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_7.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_7.setObjectName("spinBox_7")
        self.horizontalLayout_3.addWidget(self.spinBox_7)
        self.spinBox_8 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_8.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_8.setObjectName("spinBox_8")
        self.horizontalLayout_3.addWidget(self.spinBox_8)
        self.spinBox_9 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_3)
        self.spinBox_9.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_9.setObjectName("spinBox_9")
        self.horizontalLayout_3.addWidget(self.spinBox_9)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(320, 110, 81, 281))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.spinBox_11 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_11.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_11.setObjectName("spinBox_11")
        self.verticalLayout.addWidget(self.spinBox_11)
        self.spinBox_10 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_10.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_10.setObjectName("spinBox_10")
        self.verticalLayout.addWidget(self.spinBox_10)
        self.spinBox_12 = QtWidgets.QSpinBox(self.verticalLayoutWidget)
        self.spinBox_12.setStyleSheet(".QSpinBox {\n"
"  color: #fff;\n"
"  font-size: 15px;\n"
"}\n"
"\n"
".QSpinBox:hover {\n"
"  background: #2c3e50;\n"
"}\n"
"\n"
".QSpinBox:pressed {\n"
"  font-size: 14px;\n"
"}")
        self.spinBox_12.setObjectName("spinBox_12")
        self.verticalLayout.addWidget(self.spinBox_12)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 420, 181, 17))
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
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Матриця A"))
        self.label_2.setText(_translate("MainWindow", "Матриця B"))
        self.pushButton.setText(_translate("MainWindow", "Обчислити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ux = Ui_MainWindow_1()
    ux.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
