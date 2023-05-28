import math
from PyQt5.QtWidgets import QApplication


class Sort:
    def __init__(self, ui, data):
        self._arr = data
        self._ui = ui
        self._comp = 0
        self._swaps = 0
        self._recursionDepth = 0
        self._maxDepth = 0
        self._flag = True if len(self._arr) <= 300 else False

    def sort(self, left, right):
        pass

    def printArr(self):
        print(self._arr)

    def _swap(self, i, j):
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
        self._swaps += 1
        self._ui.updateCounters(1, 0, 0, 0)

    def _insertionSort(self, left, right):
        # if not self._ui.plotFlag:
        #     return
        for i in range(left, right + 1):
            j = i
            while j > left:
                self._comp += 1
                self._ui.updateCounters(0, 1, 0, 0)
                if self._arr[j - 1] > self._arr[j]:
                    self._swap(j - 1, j)
                    self._ui.updateCounters(1, 0, 0, 0)
                    if self._flag:
                        self._ui.plot(j - 1)
                        QApplication.processEvents()
                    j -= 1
                    continue
                break

    def getNumOfOperations(self):
        return self._swaps, self._comp, self._recursionDepth, self._maxDepth


class MergeSort(Sort):

    def __merge(self, left, mid, right):
        # if not self._ui.plotFlag:
        #     return

        i = left
        j = mid
        k = 0
        size = right - left + 1
        tempArr = [0] * size

        while (i < mid) and (j <= right):
            self._comp += 1
            self._ui.updateCounters(0, 1, 0, 0)
            if self._arr[i] <= self._arr[j]:
                tempArr[k] = self._arr[i]
                i += 1
            else:
                tempArr[k] = self._arr[j]
                j += 1
            k += 1

        while i < mid:
            tempArr[k] = self._arr[i]
            k += 1
            i += 1

        while j <= right:
            tempArr[k] = self._arr[j]
            k += 1
            j += 1

        k = 0

        for i in range(left, right + 1):
            # if not self._ui.plotFlag:
            #     return
            if self._flag:
                self._ui.plot(mid)
                QApplication.processEvents()
            self._arr[i] = tempArr[k]
            self._swaps += 1
            self._ui.updateCounters(1, 0, 0, 0)
            k += 1

    def sort(self, left, right):
        # if not self._ui.plotFlag:
        #     return

        self._recursionDepth += 1
        self._ui.updateCounters(0, 0, 1, 0)

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth
            self._ui.updateCounters(0, 0, 0, 1)

        if right > left:
            mid = (right + left) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.__merge(left, mid + 1, right)

        self._recursionDepth -= 1
        self._ui.updateCounters(0, 0, -1, 0)


class QuikSort(Sort):

    def __medianOf3(self, left, mid, right):
        # if not self._ui.plotFlag:
        #     return
        if self._arr[mid] < self._arr[left] < self._arr[right]:
            median = left
        elif self._arr[right] < self._arr[left] < self._arr[mid]:
            median = left
        elif self._arr[left] < self._arr[mid] < self._arr[right]:
            median = mid
        elif self._arr[right] < self._arr[mid] < self._arr[left]:
            median = mid
        else:
            median = right
        (self._arr[median], self._arr[right]) = (self._arr[right], self._arr[median])

    def __partition(self, left, right):
        # if not self._ui.plotFlag:
        #     return

        x = self._arr[right]
        pInd = left - 1

        for j in range(left, right):
            self._comp += 1
            if self._arr[j] <= x:
                pInd += 1
                self._swap(pInd, j)

        self._swap(pInd + 1, right)
        if self._flag:
            self._ui.plot(pInd + 1)
            QApplication.processEvents()
        return pInd + 1

    def sort(self, left, right):
        # if not self._ui.plotFlag:
        #     return
        if left < right:
            if (right - left + 1) <= 3:
                self._insertionSort(left, right)
            else:
                self.__medianOf3(left, (left + right) // 2, right)
                p = self.__partition(left, right)
                self.sort(left, p - 1)
                self.sort(p + 1, right)


class IntroSort(Sort):
    def __introSort(self, maxdepth):
        self._ui.updateCounters(0, 0, 0, 1)
        # if not self._ui.plotFlag:
        #     return
        n = len(self._arr)
        if n < 16:
            self._insertionSort(0, len(self._arr) - 1)
        elif maxdepth == 0:
            self.__heapSort()
        else:
            p = self.__partition()
            self.__introSort(maxdepth - 1)
            self._arr = self._arr[0:p] + self._arr[p + 1:n]
            self.__introSort(maxdepth - 1)

        self._ui.updateCounters(0, 0, -1, 1)

    def sort(self, left, right):
        # if not self._ui.plotFlag:
        #     return
        maxDepth = math.floor(math.log2(len(self._arr))) * 2
        self.__introSort(maxDepth)

    def __partition(self):
        # if not self._ui.plotFlag:
        #     return
        pivot = self._arr[-1]
        i = -1
        for j in range(len(self._arr) - 1):
            self._ui.updateCounters(1, 0, 0, 0)
            if self._arr[j] <= pivot:
                i += 1

                self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
                self._ui.updateCounters(0, 1, 0, 0)

        if self._flag:
            self._ui.plot(i)
            QApplication.processEvents()
        self._arr[i + 1], self._arr[-1] = self._arr[-1], self._arr[i + 1]
        self._ui.updateCounters(0, 1, 0, 0)
        return i + 1

    def __heapSort(self):
        # if not self._ui.plotFlag:
        #     return

        def heapify(n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self._arr[left] > self._arr[largest]:
                largest = left

            if right < n and self._arr[right] > self._arr[largest]:
                largest = right

            if largest != i:
                self._arr[i], self._arr[largest] = self._arr[largest], self._arr[i]
                self._ui.updateCounters(0, 1, 0, 0)
                heapify(n, largest)

        n = len(self._arr)

        for i in range(n // 2 - 1, -1, -1):
            heapify(n, i)

        for i in range(n - 1, 0, -1):
            # if not self._ui.plotFlag:
            #     return
            if self._flag:
                self._ui.plot(i)
                QApplication.processEvents()
            self._arr[0], self._arr[i] = self._arr[i], self._arr[0]
            self._ui.updateCounters(0, 1, 0, 0)
            heapify(i, 0)
