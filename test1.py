import heapq
import math
import random

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
        # Update counters in the UI
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

    def _insertionSort(self, left, right):
        if self._ui.flagStop:
            return
        for i in range(left, right + 1):
            j = i
            while j > left:
                self._comp += 1
                self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
                if self._arr[j - 1] > self._arr[j]:
                    self._swap(j - 1, j)
                    self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
                    if self._flag:
                        self._ui.plot(j - 1)
                        QApplication.processEvents()
                    j -= 1
                    continue
                break

    def _medianOf3(self, left, mid, right):
        if self._ui.flagStop:
            return
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
        self._swap(median, right)

    @property
    def NumOfOperations(self):
        return self._swaps, self._comp, self._recursionDepth, self._maxDepth


class MergeSort(Sort):

    def __merge(self, left, mid, right):
        if self._ui.flagStop:
            return

        i = left
        j = mid
        k = 0
        size = right - left + 1
        tempArr = [0] * size

        while (i < mid) and (j <= right):
            self._comp += 1
            self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
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
            self._swaps += 1
            self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
            k += 1

    def sort(self, left, right):
        if self._ui.flagStop:
            return

        self._recursionDepth += 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth

        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if right > left:
            mid = (right + left) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.__merge(left, mid + 1, right)

        self._recursionDepth -= 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)


class QuikSort(Sort):

    def __partition(self, left, right):
        if self._ui.flagStop:
            return

        x = self._arr[right]
        pInd = left - 1

        for j in range(left, right):
            self._comp += 1
            self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
            if self._arr[j] <= x:
                pInd += 1
                self._swap(pInd, j)

        self._swap(pInd + 1, right)
        if self._flag:
            self._ui.plot(pInd + 1)
            QApplication.processEvents()
        return pInd + 1

    def sort(self, left, right):
        if self._ui.flagStop:
            return

        self._recursionDepth += 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth
            self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if left < right:
            if (right - left + 1) <= 3:
                self._insertionSort(left, right)
            else:
                self._medianOf3(left, (left + right) // 2, right)
                p = self.__partition(left, right)
                self.sort(left, p - 1)
                self.sort(p + 1, right)

        self._recursionDepth -= 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)


class IntroSort(Sort):
    def sort(self, left, right):
        if self._ui.flagStop:
            return
        max_depth = 2 * math.floor(math.log2(len(self._arr)))
        self.__introSort(self._arr, left, right, max_depth)

    def _partition(self, low, high):
        if self._ui.flagStop:
            return
        pivot = self._arr[high]
        p_index = low

        for i in range(low, high):
            self._comp += 1
            self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

            if self._arr[i] <= pivot:
                self._swap(i, p_index)
                p_index += 1

        self._swap(p_index, high)
        return p_index

    def _rand_partition(self, low, high):
        if self._ui.flagStop:
            return
        pivot_index = random.randint(low, high)
        self._swap(pivot_index, high)
        return self._partition(low, high)

    def _heapSort(self, begin, end):
        if self._ui.flagStop:
            return
        heapq.heapify(self._arr[begin:end + 1])
        for i in range(end, begin - 1, -1):
            self._swaps += 1
            self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
            self._arr[i] = heapq.heappop(self._arr[begin:end + 1])

    def __introSort(self, arr, begin, end, max_depth):
        if self._ui.flagStop:
            return

        self._recursionDepth += 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth

        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if end - begin < 16:
            self._insertionSort(begin, end)
        elif max_depth == 0:
            self._heapSort(begin, end)
        else:
            pivot = self._rand_partition(begin, end)
            self.__introSort(arr, begin, pivot - 1, max_depth - 1)
            self.__introSort(arr, pivot + 1, end, max_depth - 1)

        self._recursionDepth -= 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)


