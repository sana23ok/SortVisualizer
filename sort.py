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
        #set flag true if animation is required
        self._flag = True if len(self._arr) <= 300 else False

    def sort(self, left, right):
        #virtual method of parent class
        pass

    # def printArr(self):
    #     print(self._arr)

    def _swap(self, i, j):
        self._arr[i], self._arr[j] = self._arr[j], self._arr[i]
        self._swaps += 1
        # Update counters in the UI
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

    def _insertionSort(self, left, right):
        # perform insertion sort on specific range of elements
        for i in range(left, right + 1):
            # check if the stop flag was set
            if self._ui.flagStop:
                return
            j = i
            # self._comp += 1
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

    def _partition(self, start, end):
        pivot = self._arr[end]
        pIndex = start
        for i in range(start, end):
            if self._ui.flagStop:
                return -1
            self._comp += 1
            if self._flag:
                self._ui.plot(i)
                QApplication.processEvents()
            if self._arr[i] <= pivot:
                self._swap(i, pIndex)
                pIndex += 1
        self._swap(pIndex, end)
        return pIndex

    @property
    def NumOfOperations(self):
        #rerturn number of operations using property
        return self._comp, self._swaps, self._recursionDepth, self._maxDepth


class MergeSort(Sort):

    def __merge(self, left, mid, right):
        if self._ui.flagStop:
            return

        # merges two subarrays within the specified range
        i = left
        j = mid
        k = 0
        size = right - left + 1
        tempArr = [0] * size

        # merge into a temporary array
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

        # copy any remaining elements
        while i < mid:
            tempArr[k] = self._arr[i]
            k += 1
            i += 1

        while j <= right:
            tempArr[k] = self._arr[j]
            k += 1
            j += 1

        k = 0

        # copy the merged elements back to the original array
        for i in range(left, right+1):
            # create plot on each merge operation
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
        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if right > left:
            mid = (right + left) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.__merge(left, mid + 1, right)

        #decrease recursion number
        self._recursionDepth -= 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)


class QuickSort(Sort):
    def __medianOf3(self, i1, i2, i3):
        # Helper function to find the median of three elements
        if (self._arr[i2] < self._arr[i1] < self._arr[i3]) or (self._arr[i3] < self._arr[i1] < self._arr[i2]):
            return i1
        elif (self._arr[i1] < self._arr[i2] < self._arr[i3]) or (self._arr[i3] < self._arr[i2] < self._arr[i1]):
            return i2
        else:
            return i3

    def __median_partition(self, start, end):
        # Partition the array using median-of-three pivot selection
        pivot = self.__medianOf3(start, (start + end) // 2, end)
        if self._flag:
            self._ui.plot(pivot)
            QApplication.processEvents()
        self._swap(pivot, end)
        return self._partition(start, end)

    def sort(self, left, right):
        if self._ui.flagStop:
            return

        self._recursionDepth += 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth

        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if left < right:
            if right - left + 1 <= 3:
                self._insertionSort(left, right)
                # self._recursionDepth -= 1
                return
            pIndex = self.__median_partition(left, right)
            if pIndex == -1:
                return
            if self._flag:
                self._ui.plot(pIndex)
                QApplication.processEvents()
            self.sort(left, pIndex - 1)
            self.sort(pIndex + 1, right)

        self._recursionDepth -= 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)


class IntroSort(Sort):
    def sort(self, left, right):
        if self._ui.flagStop:
            return
        max_depth = 2 * math.floor(math.log2(len(self._arr)))
        self.__introSort(left, right, max_depth)

    def __rand_partition(self, low, high):
        # Partition the array using random pivot selection
        pivot_index = random.randint(low, high)
        self._swap(pivot_index, high)
        return self._partition(low, high)

    def __heapSort(self, left, right):
        def heapify(parent):
            if self._ui.flagStop:
                return
            child = 2 * parent + 1
            if child < right:
                if child + 1 < right and self._arr[child] < self._arr[child + 1]:
                    child += 1
                if self._arr[parent] < self._arr[child]:
                    # self._arr[parent], self._arr[child] = self._arr[child], self._arr[parent]
                    self._swap(parent, child)
                    heapify(child)

        for i in range(math.floor((right - left) / 2), -1, -1):
            heapify(i)
        for i in range(right - 1, left, -1):
            # self._arr[left], self._arr[i] = self._arr[i], self._arr[left]
            self._swap(left, i)
            heapify(left)

    def __introSort(self, begin, end, depth_limit):
        if self._ui.flagStop:
            return

        self._recursionDepth += 1
        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)

        if end - begin < 16:
            self._insertionSort(begin, end)
        elif depth_limit == 0:
            # If the depth limit is reached, switch to heap sort
            self.__heapSort(begin, end)
        else:
            pivot = self.__rand_partition(begin, end)
            if pivot == -1:
                return
            self.__introSort(begin, pivot - 1, depth_limit - 1)
            self.__introSort(pivot + 1, end, depth_limit - 1)

        self._recursionDepth -= 1
        self._ui.updateCounters(self._comp, self._swaps, self._recursionDepth, self._maxDepth)
