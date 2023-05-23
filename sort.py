import math

from PyQt5.QtWidgets import QApplication


class Sort:
    def __init__(self, ui, data):
        self._arr = data
        self._ui = ui
        self._flag = True if len(self._arr) <= 300 else False

    def sort(self, left, right):
        pass

    def printArr(self):
        print(self._arr)


class MergeSort(Sort):

    def __merge(self, left, mid, right):
        i = left
        j = mid
        k = 0
        size = right - left + 1
        tempArr = [0] * size

        while (i < mid) and (j <= right):
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
            if self._flag:
                self._ui.plot(mid)
                QApplication.processEvents()
            self._arr[i] = tempArr[k]
            k += 1

    def sort(self, left, right):
        if right > left:
            mid = (right + left) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.__merge(left, mid + 1, right)


class QuikSort(Sort):

    def __insertionSort(self, left, right):
        for i in range(left, right + 1):
            j = i
            while j > left:
                if self._arr[j - 1] > self._arr[j]:
                    (self._arr[j - 1], self._arr[j]) = (self._arr[j], self._arr[j - 1])
                    if self._flag:
                        self._ui.plot(j - 1)
                        QApplication.processEvents()
                    j -= 1
                    continue
                break

    def __medianOf3(self, left, mid, right):
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
        x = self._arr[right]
        pInd = left - 1

        for j in range(left, right):
            if self._arr[j] <= x:
                pInd += 1
                self._arr[pInd], self._arr[j] = self._arr[j], self._arr[pInd]

        self._arr[pInd + 1], self._arr[right] = self._arr[right], self._arr[pInd + 1]
        if self._flag:
            self._ui.plot(pInd + 1)
            QApplication.processEvents()
        return pInd + 1

    def sort(self, left, right):
        if left < right:
            if (right - left + 1) <= 3:
                self.__insertionSort(left, right)
            else:
                self.__medianOf3(left, (left + right) // 2, right)
                p = self.__partition(left, right)
                self.sort(left, p - 1)
                self.sort(p + 1, right)


class IntroSort(Sort):

    def __partition(self, left, right):
        pivot = self._arr[left]
        i = left - 1
        j = right

        while True:
            i += 1
            while self._arr[i] < pivot:
                i += 1
            j -= 1
            while self._arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
            if self._flag:
                self._ui.plot(i)
                QApplication.processEvents()

    def __heapSort(self, left, right):
        def heapify(parent):
            child = 2 * parent + 1
            if child < right:
                if child + 1 < right and self._arr[child] < self._arr[child + 1]:
                    child += 1
                if self._arr[parent] < self._arr[child]:
                    self._arr[parent], self._arr[child] = self._arr[child], self._arr[parent]
                    heapify(child)

        for i in range(math.floor((right - left) / 2), -1, -1):
            heapify(i)
        for i in range(right - 1, left, -1):
            self._arr[left], self._arr[i] = self._arr[i], self._arr[left]
            heapify(left)

    def sort(self, left, right):
        depth_limit = 2 * math.floor(math.log(len(self._arr)))
        if right - left <= 1:
            return
        elif depth_limit == 0:
            self.__heapSort(left, right)
        else:
            p = self.__partition(left, right)
            self.sort(left, p + 1)
            self.sort(p + 1, right)

