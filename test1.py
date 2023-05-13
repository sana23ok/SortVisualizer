import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from numpy import random
import numpy as np
from class_sort import Sort


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(957, 523)
        MainWindow.setStyleSheet("background-color:rgb(219, 239, 230)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        #self.StartBtn = QtWidgets.QPushButton(self.PlotFrame, clicked=lambda: self.plotOnCanvas())
        self.StartBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.plotOnCanvas())
        self.StartBtn.setGeometry(QtCore.QRect(720, 370, 141, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.StartBtn.setFont(font)
        self.StartBtn.setMouseTracking(False)
        self.StartBtn.setStyleSheet("QPushButton{\n"
                                    "background-color:rgb(105, 133, 255);\n"
                                    "border-style:outset;\n"
                                    "border-with:2px;\n"
                                    "border-radius:8px;\n"
                                    "}\n"
                                    "QPushButton:pressed{\n"
                                    " background-color:rgb(85, 120, 250);\n"
                                    "}\n"
                                    "")
        self.StartBtn.setObjectName("StartBtn")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(640, 20, 301, 261))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.labelSize = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelSize.setFont(font)
        self.labelSize.setStyleSheet("color:rgb(0,0,0);")
        self.labelSize.setObjectName("labelSize")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.labelSize)
        self.spinBox_Size = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_Size.setStyleSheet("color:rgb(0, 0, 0);")
        self.spinBox_Size.setMinimum(100)
        self.spinBox_Size.setMaximum(50000)
        self.spinBox_Size.setProperty("value", 100)
        self.spinBox_Size.setObjectName("spinBox_Size")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.spinBox_Size)
        self.spinBox_limitA = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_limitA.setStyleSheet("color:rgb(0, 0, 0);")
        self.spinBox_limitA.setMinimum(0)
        self.spinBox_limitA.setMaximum(50000)
        self.spinBox_limitA.setProperty("value", 0)
        self.spinBox_limitA.setObjectName("spinBox_limitA")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.spinBox_limitA)
        self.labelBorderA = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelBorderA.setFont(font)
        self.labelBorderA.setStyleSheet("color:rgb(0,0,0);")
        self.labelBorderA.setObjectName("labelBorderA")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.labelBorderA)
        self.labelBorderB = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.labelBorderB.setFont(font)
        self.labelBorderB.setStyleSheet("color:rgb(0,0,0);")
        self.labelBorderB.setObjectName("labelBorderB")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.labelBorderB)
        self.spinBox_limitB = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.spinBox_limitB.setStyleSheet("color:rgb(0, 0, 0);")
        self.spinBox_limitB.setMinimum(0)
        self.spinBox_limitB.setMaximum(50000)
        self.spinBox_limitB.setProperty("value", 0)
        self.spinBox_limitB.setObjectName("spinBox_limitB")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.spinBox_limitB)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.FieldRole, spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtWidgets.QFormLayout.FieldRole, spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(5, QtWidgets.QFormLayout.FieldRole, spacerItem2)
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        self.comboBox.setStyleSheet("color:rgb(0, 15, 0);\n"
                                    "color-back-ground:rgb(126, 255, 245);\n"
                                    "")
        self.comboBox.setObjectName("comboBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox)

        #frame where pyPlot is going to be located
        self.PlotFrame = QtWidgets.QFrame(self.centralwidget)
        self.PlotFrame.setGeometry(QtCore.QRect(40, 30, 571, 451))
        self.PlotFrame.setObjectName("PlotFrame")
        #create horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.PlotFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        ##Canvas here
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        ## end of Canvas
        ## Add Canvas
        self.horizontalLayout.addWidget(self.canvas)
        ## end of horizontal layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PlotFrame)
        self.verticalLayout.setObjectName("verticalLayout")

        #self.StartBtn = QtWidgets.QPushButton(self.PlotFrame, clicked=lambda : self.plotOnCanvas())

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.StartBtn.setText(_translate("MainWindow", "Sort"))
        self.labelSize.setText(_translate("MainWindow", "Size of array:"))
        self.labelBorderA.setText(_translate("MainWindow", "First element:"))
        self.labelBorderB.setText(_translate("MainWindow", "Last element:"))

    def plotOnCanvas(self):
        ##clesr the canvas
        self.figure.clear()
        x=["apple", "orange", "coconuts", "pawpaw"]
        value= random.randint(50, size=4)
        print(value)

        #create the plot

        plt.bar(x, value, color="cyan", width=0.4)
        plt.xlabel("type of fruits")
        plt.ylabel("no. of fruits")
        plt.title("Random fruit in the basket")
        #refresh
        self.canvas.draw()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
