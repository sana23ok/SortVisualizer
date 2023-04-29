# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'intf.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-color:rgb(27, 27, 27);\n"
                                 "")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.spinBox_Size = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_Size.setGeometry(QtCore.QRect(180, 60, 141, 31))
        self.spinBox_Size.setStyleSheet("color:rgb(255, 255, 255);")
        self.spinBox_Size.setMinimum(100)
        self.spinBox_Size.setMaximum(50000)
        self.spinBox_Size.setProperty("value", 100)
        self.spinBox_Size.setObjectName("spinBox_Size")
        self.spinBox_limitA = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_limitA.setGeometry(QtCore.QRect(570, 60, 141, 31))
        self.spinBox_limitA.setStyleSheet("color:rgb(255, 255, 255);")
        self.spinBox_limitA.setMinimum(0)
        self.spinBox_limitA.setMaximum(50000)
        self.spinBox_limitA.setProperty("value", 0)
        self.spinBox_limitA.setObjectName("spinBox_limitA")
        self.spinBox_limitB = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_limitB.setGeometry(QtCore.QRect(570, 120, 141, 31))
        self.spinBox_limitB.setStyleSheet("color:rgb(255, 255, 255);")
        self.spinBox_limitB.setMinimum(0)
        self.spinBox_limitB.setMaximum(50000)
        self.spinBox_limitB.setProperty("value", 0)
        self.spinBox_limitB.setObjectName("spinBox_limitB")
        self.labelSize = QtWidgets.QLabel(self.centralwidget)
        self.labelSize.setGeometry(QtCore.QRect(40, 60, 110, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelSize.setFont(font)
        self.labelSize.setStyleSheet("color:rgb(255, 255, 255);")
        self.labelSize.setObjectName("labelSize")
        self.labelBorderA = QtWidgets.QLabel(self.centralwidget)
        self.labelBorderA.setGeometry(QtCore.QRect(430, 60, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelBorderA.setFont(font)
        self.labelBorderA.setStyleSheet("color:rgb(255, 255, 255);")
        self.labelBorderA.setObjectName("labelBorderA")
        self.labelBorderB = QtWidgets.QLabel(self.centralwidget)
        self.labelBorderB.setGeometry(QtCore.QRect(430, 120, 130, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelBorderB.setFont(font)
        self.labelBorderB.setStyleSheet("color:rgb(255, 255, 255);")
        self.labelBorderB.setObjectName("labelBorderB")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 470, 118, 23))
        self.progressBar.setStyleSheet("color:rgb(255, 255, 255);")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButtonStart = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart.setGeometry(QtCore.QRect(40, 390, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonStart.setFont(font)
        self.pushButtonStart.setMouseTracking(False)
        self.pushButtonStart.setStyleSheet("background-color:rgb(105, 133, 255);\n"
                                           "border-style:outset;\n"
                                           "border-with:2px;\n"
                                           "border-radius:8px;")
        self.pushButtonStart.setObjectName("pushButtonStart")
        self.pushButtonStart_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart_2.setGeometry(QtCore.QRect(40, 310, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonStart_2.setFont(font)
        self.pushButtonStart_2.setMouseTracking(False)
        self.pushButtonStart_2.setStyleSheet("background-color:rgb(105, 133, 255);\n"
                                             "border-style:outset;\n"
                                             "border-with:2px;\n"
                                             "border-radius:8px;")
        self.pushButtonStart_2.setObjectName("pushButtonStart_2")
        self.pushButtonStart_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStart_3.setGeometry(QtCore.QRect(40, 230, 130, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButtonStart_3.setFont(font)
        self.pushButtonStart_3.setMouseTracking(False)
        self.pushButtonStart_3.setStyleSheet("background-color:rgb(105, 133, 255);\n"
                                             "border-style:outset;\n"
                                             "border-with:2px;\n"
                                             "border-radius:8px;")
        self.pushButtonStart_3.setObjectName("pushButtonStart_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.labelSize.setText(_translate("MainWindow", "Size of array:"))
        self.labelBorderA.setText(_translate("MainWindow", "First element:"))
        self.labelBorderB.setText(_translate("MainWindow", "Last element:"))
        self.pushButtonStart.setText(_translate("MainWindow", "Intro Sort"))
        self.pushButtonStart_2.setText(_translate("MainWindow", "Quick Sort"))
        self.pushButtonStart_3.setText(_translate("MainWindow", "Merge Sort"))

