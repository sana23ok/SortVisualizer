import os
import shutil
import sys
import time
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont, QLinearGradient, QBrush, QPalette, QColor
from PyQt5.QtWidgets import QApplication, QMessageBox, QLabel
from matplotlib import pyplot as plt
from matplotlib.backends.backend_template import FigureCanvas
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from sort import MergeSort, QuickSort, IntroSort
from random import randint
import FileCreator


def show_message_box(title, message, icon=QMessageBox.Information):
    # Create a QMessageBox instance
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(message)
    # Set the icon
    msg_box.setIcon(icon)
    # Add buttons (optional)
    msg_box.addButton(QMessageBox.Ok)
    # msg_box.addButton(QMessageBox.Cancel)
    clicked_button = msg_box.exec_()


def generate_array(a, b, size):
    arr = []
    i = 0
    while i != size:
        temp = randint(a, b)
        # if temp not in arr:
        arr.append(temp)
        i += 1
    return arr


def fillScrollArea(area, arr):
    # display unsorted array
    array_text = '\n'.join(arr)
    labelS = QLabel(array_text)
    font = labelS.font()
    # font.setBold(True)
    font.setItalic(True)
    font.setPointSize(12)
    labelS.setFont(font)
    area.setWidget(labelS)


def clearScrollArea(area):
    # Check if the scroll area is filled
    if area.widget():
        # Clear the contents of the scroll area
        widget = area.takeWidget()
        widget.deleteLater()
        area.setWidgetResizable(True)


def setPl(obj):
    obj.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
    # Create a palette object
    palette = QtGui.QPalette()
    lcdColor = QtGui.QColor(65, 105, 225)
    palette.setColor(QtGui.QPalette.WindowText, lcdColor)
    obj.setPalette(palette)


def settingsForSpinBox(obj, min, max, val, name):
    obj.setMinimum(min)
    obj.setMaximum(max)
    obj.setProperty("value", val)
    obj.setObjectName(name)
    obj.setStyleSheet("background-color: rgb(201, 217, 235);")


def settingsForComboBox(obj, font, names, objName):
    obj.setFont(font)
    obj.addItems(names)
    obj.setObjectName(objName)
    obj.setStyleSheet("background-color: rgb(201, 217, 235);")


def setLabel(obj, size, weight, name, style="color:rgb(0,0,0);"):
    font = QtGui.QFont()
    font.setPointSize(size)
    # font.setBold(True)
    # font.setItalic(True)
    font.setWeight(weight)
    obj.setFont(font)
    obj.setStyleSheet(style)
    obj.setObjectName(name)


def setButton(obj, pointSize, name, style="QPushButton{\n"
                                          "background-color:rgb(105, 133, 255);\n"
                                          "border-style:outset;\n"
                                          "border-with:2px;\n"
                                          "border-radius:8px;\n"
                                          "}\n"
                                          "QPushButton:pressed{\n"
                                          " background-color:rgb(85, 120, 250);\n"
                                          "}\n"
                                          ""):

    font = QtGui.QFont()
    font.setPointSize(pointSize)
    obj.setFont(font)
    obj.setMouseTracking(False)
    obj.setStyleSheet(style)
    obj.setObjectName(name)


def setLineEdit(nameField, font, name, param1):
    font = QFont()
    font.setPointSize(font)
    nameField.setFont(font)
    nameField.setObjectName(name)
    nameField.setPlaceholderText(param1)


class Ui_MainWindow(object):

    def __init__(self):
        self.__SORT = None
        self.__resultFile = None
        self.__name = "temp.txt"
        self.__resultFile = FileCreator.File(self.__name)
        self.flagStop = False
        self.__generationFlag = False
        self.__saveFlag = False
        #size of array
        self.__n = None
        self.__lst = []
        # self.sortingTime = 5
        self.font = QFont("Arial", 10)
        self.__algoNamesList = ['Merge Sort', 'Quick Sort', 'Intro Sort']
        self.__choice = None
        self.__unordered = False

    def setupUi(self, MainWindow):
        # main window settings
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 880)
        MainWindow.setMinimumSize(QtCore.QSize(60, 120))
        MainWindow.setBaseSize(QtCore.QSize(5, 5))
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)

        palette = MainWindow.palette()
        gradient = QLinearGradient(0, 0, 0, MainWindow.height())

        gradient.setColorAt(0, QColor(65, 105, 226))
        # gradient.setColorAt(0, QColor(143, 163, 225))
        gradient.setColorAt(1, QColor(0, 0, 100))

        brush = QBrush(gradient)
        palette.setBrush(QPalette.Background, brush)
        MainWindow.setPalette(palette)

        # MainWindow.setStyleSheet("background-color:rgb(173, 216, 230)")

        # central widget
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 30, 321, 361))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.formLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        # slider settings
        self.horizontalSlider = QtWidgets.QSlider(self.formLayoutWidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(1)  # Set the minimum value to 1
        self.horizontalSlider.setMaximum(100000)
        self.horizontalSlider.setSingleStep(100000)  # Set the step size to 1
        # Optional: Set the default value to a specific position within the range
        self.horizontalSlider.setValue(50000)
        self.horizontalSlider.setProperty("value", 500)
        # Connect the valueChanged signal to the updateSliderValue slot
        # self.horizontalSlider.valueChanged.connect(lambda: self.updateSliderValue(self.horizontalSlider.value()))
        self.gridLayout.addWidget(self.horizontalSlider, 12, 0, 1, 1)

        # setting for comboBox
        self.comboBox = QtWidgets.QComboBox(self.formLayoutWidget)
        settingsForComboBox(self.comboBox, self.font, self.__algoNamesList, "comboBox")
        # connect combo box with action
        self.comboBox.currentIndexChanged.connect(lambda: self.__comboBoxChanged(self.comboBox.currentText()))

        self.gridLayout.addWidget(self.comboBox, 10, 0, 1, 1)

        # налаштування кожного надпису, кнопки і тд в окремих ф-ціях
        # spin box to get size of array
        self.spinBox_Size = QtWidgets.QSpinBox(self.formLayoutWidget)
        # settingsForSpinBox(obj, min, max, val, name):
        settingsForSpinBox(self.spinBox_Size, 10, 50000, 100, "spinBox_Size")

        self.gridLayout.addWidget(self.spinBox_Size, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 5, 0, 1, 1)

        # spin box to get value of first element
        self.spinBox_limitA = QtWidgets.QSpinBox(self.formLayoutWidget)
        settingsForSpinBox(self.spinBox_limitA, 0, 2000000, 0, "spinBox_limitA")

        self.gridLayout.addWidget(self.spinBox_limitA, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)

        # spin box to get value of last element
        self.spinBox_limitB = QtWidgets.QSpinBox(self.formLayoutWidget)
        settingsForSpinBox(self.spinBox_limitB, 100, 2000000, 100, "spinBox_limitB")
        self.gridLayout.addWidget(self.spinBox_limitB, 6, 0, 1, 1)
        # labels and settings for them
        # label for size of array
        self.labelSize = QtWidgets.QLabel(self.formLayoutWidget)
        setLabel(self.labelSize, 10, 50, "labelSize")
        self.gridLayout.addWidget(self.labelSize, 0, 1, 1, 1)
        # label for 1st element in array
        self.labelBorderA = QtWidgets.QLabel(self.formLayoutWidget)
        setLabel(self.labelBorderA, 10, 50, "labelBorderA ")
        self.gridLayout.addWidget(self.labelBorderA, 3, 1, 1, 1)
        # label for last element in array
        self.labelBorderB = QtWidgets.QLabel(self.formLayoutWidget)
        setLabel(self.labelBorderB, 10, 50, "labelBorderB")
        self.gridLayout.addWidget(self.labelBorderB, 6, 1, 1, 1)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem2, 8, 0, 1, 1)
        # label for name of algo
        self.AlgoLabel = QtWidgets.QLabel(self.formLayoutWidget)
        setLabel(self.AlgoLabel, 10, 50, "AlgoLabel")
        self.gridLayout.addWidget(self.AlgoLabel, 10, 1, 1, 1)
        # label speed slider
        self.SpeedLabel = QtWidgets.QLabel(self.formLayoutWidget)
        setLabel(self.SpeedLabel, 10, 50, "SpeedLabel")
        self.gridLayout.addWidget(self.SpeedLabel, 12, 1, 1, 1)

        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 11, 0, 1, 1)

        self.PlotFrame = QtWidgets.QFrame(self.centralwidget)
        self.PlotFrame.setGeometry(QtCore.QRect(400, 6, 900, 470))
        self.PlotFrame.setObjectName("PlotFrame")
        # embed graph
        # frame where pyPlot is going to be located
        # create horizontal layout
        self.horizontalLayout = QtWidgets.QVBoxLayout(self.PlotFrame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # Canvas here
        # Create a Figure object and adjust its size
        self.figure = plt.figure(figsize=(8, 6))
        # Add canvas | End canvas
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.canvas.updateGeometry()
        self.canvas = FigureCanvas(self.figure)
        # create vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.PlotFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout.addWidget(self.canvas)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        # end of horizontal layout

        # button to start sorting
        self.StartBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.__plotOnCanvas())
        self.StartBtn.setGeometry(QtCore.QRect(160, 410, 101, 31))
        setButton(self.StartBtn, 10, "StartBtn")

        self.GenerationBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.__generate())
        self.GenerationBtn.setGeometry(QtCore.QRect(50, 410, 101, 31))
        setButton(self.GenerationBtn, 10, "GenerationBtn")

        self.StopBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.__setStopFlag())
        self.StopBtn.setGeometry(QtCore.QRect(270, 410, 101, 31))
        setButton(self.StopBtn, 10, "StopBtn")

        self.SaveBtn = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.__save())
        self.SaveBtn.setEnabled(True)
        self.SaveBtn.setGeometry(QtCore.QRect(1000, 712, 195, 35))
        setButton(self.SaveBtn, 10, "StartBtn")

        self.formLayoutWidgetForScrollAreas = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidgetForScrollAreas.setGeometry(QtCore.QRect(40, 490, 701, 350))
        self.formLayoutWidgetForScrollAreas.setObjectName("formLayoutWidget_2")
        self.gridLayoutScroll = QtWidgets.QGridLayout(self.formLayoutWidgetForScrollAreas)
        self.gridLayoutScroll.setContentsMargins(0, 0, 0, 0)
        self.gridLayoutScroll.setObjectName("gridLayout_2")
        spacerItem6 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayoutScroll.addItem(spacerItem6, 0, 1, 1, 1)

        # scroll area for sorted array
        self.scrollAreaS = QtWidgets.QScrollArea(self.formLayoutWidgetForScrollAreas)
        self.scrollAreaS.setMinimumSize(QtCore.QSize(320, 320))
        self.scrollAreaS.setWidgetResizable(True)
        self.scrollAreaS.setObjectName("scrollAreaS")
        self.scrollAreaS.setStyleSheet("background-color: rgb(100,149,237)")

        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 331, 318))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.scrollAreaS.setWidget(self.scrollAreaWidgetContents_3)

        # display sorted array in scroll area
        self.gridLayoutScroll.addWidget(self.scrollAreaS, 1, 0, 1, 1)

        self.UnordArrLabel = QtWidgets.QLabel(self.formLayoutWidgetForScrollAreas)
        setLabel(self.UnordArrLabel, 10, 50, "UnordArrLabel")
        self.gridLayoutScroll.addWidget(self.UnordArrLabel, 0, 2, 1, 1)

        self.SortArrayLabel = QtWidgets.QLabel(self.formLayoutWidgetForScrollAreas)
        setLabel(self.SortArrayLabel, 10, 50, "SortArrayLabel")
        self.gridLayoutScroll.addWidget(self.SortArrayLabel, 0, 0, 1, 1)

        # scroll area for unsorted
        self.scrollAreaUS = QtWidgets.QScrollArea(self.formLayoutWidgetForScrollAreas)
        self.scrollAreaUS.setMinimumSize(QtCore.QSize(320, 320))
        self.scrollAreaUS.setWidgetResizable(True)
        self.scrollAreaUS.setObjectName("scrollAreaUS")
        self.scrollAreaUS.setStyleSheet("background-color: rgb(100,149,237)")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 330, 318))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")

        self.scrollAreaUS.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayoutScroll.addWidget(self.scrollAreaUS, 1, 2, 1, 1)
        self.verticalLayoutWidgetCounters = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidgetCounters.setGeometry(QtCore.QRect(770, 490, 190, 255))
        self.verticalLayoutWidgetCounters.setObjectName("verticalLayoutWidget_2")
        self.LayoutOperationsLeft = QtWidgets.QVBoxLayout(self.verticalLayoutWidgetCounters)
        self.LayoutOperationsLeft.setContentsMargins(0, 0, 0, 0)
        self.LayoutOperationsLeft.setObjectName("verticalLayout_3")

        self.labelComp = QtWidgets.QLabel(self.verticalLayoutWidgetCounters)
        setLabel(self.labelComp, 10, 20, "labelComp")
        self.labelComp.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LayoutOperationsLeft.addWidget(self.labelComp)

        self.lcdComp = QtWidgets.QLCDNumber(self.verticalLayoutWidgetCounters)
        self.lcdComp.setObjectName("lcdNumber")
        self.lcdComp.setDigitCount(10)
        self.LayoutOperationsLeft.addWidget(self.lcdComp)
        setPl(self.lcdComp)

        spacerItem5 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LayoutOperationsLeft.addItem(spacerItem5)

        self.labelSwap = QtWidgets.QLabel(self.verticalLayoutWidgetCounters)
        setLabel(self.labelSwap, 10, 20, "labelSwap")
        self.labelSwap.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LayoutOperationsLeft.addWidget(self.labelSwap)

        self.lcdSwap= QtWidgets.QLCDNumber(self.verticalLayoutWidgetCounters)
        self.lcdSwap.setObjectName("lcdSwap")
        self.lcdSwap.setDigitCount(10)
        self.LayoutOperationsLeft.addWidget(self.lcdSwap)
        setPl(self.lcdSwap)

        spacerItem6 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LayoutOperationsLeft.addItem(spacerItem6)

        self.labelFile = QtWidgets.QLabel(self.verticalLayoutWidgetCounters)
        setLabel(self.labelFile, 10, 20, "labelFile")
        self.labelFile.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LayoutOperationsLeft.addWidget(self.labelFile)

        self.nameField = QtWidgets.QLineEdit(self.verticalLayoutWidgetCounters)
        self.nameField.setObjectName("nameField")
        self.nameField.setStyleSheet("background-color: rgb(201,217,235)")
        self.nameField.setFixedHeight(35)
        self.LayoutOperationsLeft.addWidget(self.nameField)

        self.verticalLayoutWidgetCountersRight = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidgetCountersRight.setGeometry(QtCore.QRect(1000, 490, 190, 163))
        self.verticalLayoutWidgetCountersRight.setObjectName("verticalLayoutWidget_3")

        self.LayoutOperationsRight = QtWidgets.QVBoxLayout(self.verticalLayoutWidgetCountersRight)
        self.LayoutOperationsRight.setContentsMargins(0, 0, 0, 0)
        self.LayoutOperationsRight.setObjectName("verticalLayout_4")

        self.labelRecursion = QtWidgets.QLabel(self.verticalLayoutWidgetCountersRight)
        setLabel(self.labelRecursion, 10, 20, "labelRecursion")
        self.labelRecursion.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LayoutOperationsRight.addWidget(self.labelRecursion)

        self.lcdRec = QtWidgets.QLCDNumber(self.verticalLayoutWidgetCountersRight)
        self.lcdRec.setObjectName("lcdRec")
        self.lcdRec.setDigitCount(10)
        self.LayoutOperationsRight.addWidget(self.lcdRec)
        setPl(self.lcdRec)

        spacerItem7 = QtWidgets.QSpacerItem(10, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.LayoutOperationsRight.addItem(spacerItem7)

        self.labelMaxDepth = QtWidgets.QLabel(self.verticalLayoutWidgetCountersRight)
        setLabel(self.labelMaxDepth, 10, 20, "labelMaxDepth")
        self.labelMaxDepth.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.LayoutOperationsRight.addWidget(self.labelMaxDepth)

        self.lcdMaxD = QtWidgets.QLCDNumber(self.verticalLayoutWidgetCountersRight)
        self.lcdMaxD.setObjectName("lcdMaxD")
        self.lcdMaxD.setDigitCount(10)
        self.LayoutOperationsRight.addWidget(self.lcdMaxD)
        setPl(self.lcdMaxD)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.__retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def __retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sort visualizer"))
        self.labelSize.setText(_translate("MainWindow", "Size of array"))
        self.labelBorderA.setText(_translate("MainWindow", "First element"))
        self.labelBorderB.setText(_translate("MainWindow", "Last element"))
        self.AlgoLabel.setText(_translate("MainWindow", "Algorithm"))
        self.SpeedLabel.setText(_translate("MainWindow", "Speed"))
        self.StartBtn.setText(_translate("MainWindow", "Sort"))
        self.GenerationBtn.setText(_translate("MainWindow", "Generate"))
        self.StopBtn.setText(_translate("MainWindow", "Stop"))
        self.SaveBtn.setText(_translate("MainWindow", "Save"))
        self.UnordArrLabel.setText(_translate("MainWindow", "Unsorted array"))
        self.SortArrayLabel.setText(_translate("MainWindow", "Sorted array"))
        self.labelComp.setText(_translate("MainWindow", "Comparisons:"))
        self.labelSwap.setText(_translate("MainWindow", "Swaps:"))
        self.labelFile.setText(_translate("MainWindow", "Name of file:"))
        self.labelRecursion.setText(_translate("MainWindow", "Recursion depth:"))
        self.labelMaxDepth.setText(_translate("MainWindow", "Max depht:"))
        self.GenerationBtn.setText(_translate("MainWindow", "Generate"))

    def __ani_time(self):
        # Determine sort wait time scaled to bars amount
        ani_interval = self.horizontalSlider.value()/1000000
        return ani_interval

    def __comboBoxChanged(self, name):
        self.__choice = name

    def __buttonsStatus(self, flag):
        # self.horizontalSlider.setDisabled(flag)
        self.StartBtn.setDisabled(flag)
        self.GenerationBtn.setDisabled(flag)
        self.SaveBtn.setDisabled(flag)

    def updateCounters(self,  comp=0, swaps=0, recDepth=0, maxDepth=0):
        self.lcdSwap.display(swaps)
        self.lcdComp.display(comp)
        self.lcdRec.display(recDepth)
        self.lcdMaxD.display(maxDepth)

    def __save(self):
        if self.nameField.text() and os.path.exists(self.__name):
            new_filename = self.nameField.text()+".txt"
            shutil.copy2(self.__name, new_filename)
            if self.__unordered:
                show_message_box(f"Successfully saved", f"Array is not sorted!\nSaved in {self.nameField.text()}.txt")
            else:
                show_message_box(f"Successfully saved", f"Successfully saved in {self.nameField.text()}.txt")

        elif not self.nameField.text():
            show_message_box("Name is not entered", "Enter name of the file!")
        else:
            show_message_box("Unexpected error", "Error has occurred, check entered data!")

    def __setStopFlag(self):
        self.flagStop=True

    def __checkInterval(self):
        n = self.__n
        a = self.spinBox_limitA.value()
        b = self.spinBox_limitB.value()

        if b==2000000 and a>b-n:
            show_message_box("Invalid interval", "Interval is invalid! \nDefault values are set.")
            self.spinBox_limitA.setValue(2000000-n)
            return 2000000-n, b
        elif b<a or (b-a)<n:
            show_message_box("Invalid interval", "Interval is invalid! \nDefault values are set.")
            self.spinBox_limitB.setValue(a + n)  # b equal to a + n
            return a, a + n

        return a, b

    def __generate(self):
        self.__unordered=True
        self.updateCounters()
        clearScrollArea(self.scrollAreaS)
        self.__generationFlag = True
        self.__n = self.spinBox_Size.value()
        # Generate the data to sort
        try:
            a, b = self.__checkInterval()
            self.__lst = generate_array(a, b, self.__n)
            self.__resultFile.saveInTxtFile(self.__lst, 'w')
            fillScrollArea(self.scrollAreaUS, FileCreator.convert(self.__lst))
            ui.plot()
        except Exception as e:
            # Handle the exception
            show_message_box("Error", f"An error occurred during data generation: {str(e)}", QMessageBox.Critical)

    def __plotOnCanvas(self):
        if not self.__generationFlag:
            self.__generate()
        # Set up the animation timer
        self.timer = self.canvas.new_timer(interval=100,
                                           callbacks=[(self.__startSorting, [], {})])
        # Start the sorting algorithm
        self.timer.start()

    def __startSorting(self):
        self.updateCounters(0, 0, 0, 0)
        self.__buttonsStatus(True)
        # Update the plot
        self.plot()
        QApplication.processEvents()
        algorithm_classes = {
            self.__algoNamesList[0]: MergeSort,
            self.__algoNamesList[1]: QuickSort,
            self.__algoNamesList[2]: IntroSort,
            None: MergeSort
        }

        try:
            self.__SORT = algorithm_classes.get(self.__choice)(self, self.__lst)
            self.__SORT.sort(0, self.__n - 1)
        except Exception as e:
            # Handle the exception here
            show_message_box("Error", f"An error occurred during data sorting: {str(e)}", QMessageBox.Critical)
            raise Exception("An error occurred during sorting.") from e
        self.__unordered=False
        fillScrollArea(self.scrollAreaS, FileCreator.convert(self.__lst))
        if not self.__saveFlag:
            self.__resultFile.saveInTxtFile(self.__lst, 'a')
        # SORT.printArr()
        x, y, z, v = self.__SORT.NumOfOperations
        # print("Number of swaps:", x)
        # print("Number of comparisons:", y)
        # print("Recursion depth:", z)
        # print("Max depth:", v)
        self.__resultFile.appendOperations(x, y, z, v)
        self.updateCounters(x, y, 0, v)
        if self.__n <= 300:
            ui.plot()
        self.timer.stop()
        self.__buttonsStatus(False)
        if not self.flagStop:
            self.__generationFlag = False
        else:
            self.__unordered = True
            # self.flagStop=False
        self.flagStop = False

    def plot(self, highlighted_index=0):
        # Clear the previous plot
        self.figure.clear()
        time.sleep(self.__ani_time())
        # from time.sleep(0.1) to time.sleep(0.00000001)
        ax = self.figure.add_subplot(111)

        # Plot the bars with the color
        if len(self.__lst) > 300:
            colors = ['gray'] * min(self.__n, 100)  # default color, display only 100 bars
            highlighted_index = 0
            colors[highlighted_index] = 'gray'
        else:
            colors = ['royalblue'] * self.__n  # default color
            colors[highlighted_index] = 'navy'

        ax.set_facecolor('white')
        self.x = np.arange(0, self.__n, 1)
        ax.bar(self.x[:min(self.__n, 300)], self.__lst[:min(self.__n, 300)], color=colors, width=1)

        # if self.n>300:
        #     ax.bar(self.x[:min(self.n, 100)], self.lst[:min(self.n, 100)], color=colors, width=1)

        # Remove unnecessary elements and change their color to white
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['top'].set_color('white')
        ax.spines['right'].set_color('white')
        ax.spines['left'].set_color('white')
        ax.spines['bottom'].set_color('white')
        ax.tick_params(axis='both', which='both', length=0, labelsize=0,
                       color='white')  # Remove ticks on the axes and set color to white

        # Add a legend for the marked element and sorting disabled
        if len(self.__lst) > 300:
            legend_labels = ['Animation is disabled \nif array bigger than 300']
            legend_handles = [plt.Rectangle((0, 0), 1, 1, color='lightgray')]
        else:
            legend_labels = ['']  # Replace with your desired legend labels
            legend_handles = [plt.Rectangle((0, 0), 1, 1, color='navy')]

        ax.legend(legend_handles, legend_labels, loc='lower right', ncol=2)
        # Adjust the layout to make space for the legend under the plot
        plt.subplots_adjust(left=0.02, right=1, bottom=0.02)

        # Redraw the canvas
        self.canvas.draw()

    @property
    def nameOfFile(self):
        return self.__name


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    FileCreator.deleteFile(ui.nameOfFile)
    sys.exit(app.exec_())

