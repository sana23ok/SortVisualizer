import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QSizePolicy
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


def merge(arr, left, mid, right):
    i = left
    j = mid
    k = 0
    size = right - left + 1
    tempArr = [0] * size

    while (i < mid) and (j <= right):
        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            i += 1
        else:
            tempArr[k] = arr[j]
            j += 1
        k += 1

    while i < mid:
        tempArr[k] = arr[i]
        k += 1
        i += 1

    while j <= right:
        tempArr[k] = arr[j]
        k += 1
        j += 1

    k = 0

    for i in range(left, right + 1):
        arr[i] = tempArr[k]
        k += 1


def mergeSort(arr, left, right):
    if right > left:
        mid = (right + left) // 2
        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)
        merge(arr, left, mid + 1, right)

class BubbleSortWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set up the window
        self.setWindowTitle("Bubble Sort Animation")
        self.setGeometry(100, 100, 800, 600)

        # Create a Matplotlib figure and canvas widget
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.setCentralWidget(self.canvas)

        # Set the size policy of the canvas widget to Expanding
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Generate the data to sort
        self.amount = 15
        self.lst = np.random.randint(0, 100, self.amount)
        self.x = np.arange(0, self.amount, 1)

        # Set up the animation timer
        self.timer = self.canvas.new_timer(interval=100, callbacks=[(self.animate, [], {})])

        # Start the sorting algorithm
        self.i = 0
        self.j = 0
        self.sort()

    def sort(self):
        # Bubble sort algorithm
        self.n = len(self.lst)
        self.timer.start()

    def animate(self):
        # Update the plot and wait for a short time
        self.plot()
        QApplication.processEvents()

        if self.j < self.n - self.i - 1:
            if self.lst[self.j] > self.lst[self.j + 1]:
                self.lst[self.j], self.lst[self.j + 1] = self.lst[self.j + 1], self.lst[self.j]
            self.j += 1
        else:
            self.j = 0
            self.i += 1

        if self.i == self.n - 1:
            self.timer.stop()

    def plot(self):
        # Clear the previous plot and plot the current state of the list
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.bar(self.x, self.lst)
        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = BubbleSortWindow()
    window.show()
    sys.exit(app.exec_())

