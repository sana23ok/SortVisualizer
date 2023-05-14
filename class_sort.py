import math


class Sort:
    def __init__(self, data):
        self.arr = data

    def sort(self, left, right):
        pass

    def printArr(self):
        print(self.arr)


class MergeSort(Sort):

    def __merge(self, left, mid, right):
        i = left
        j = mid
        k = 0
        size = right - left + 1
        tempArr = [0] * size

        while (i < mid) and (j <= right):
            if self.arr[i] <= self.arr[j]:
                tempArr[k] = self.arr[i]
                i += 1
            else:
                tempArr[k] = self.arr[j]
                j += 1
            k += 1

        while i < mid:
            tempArr[k] = self.arr[i]
            k += 1
            i += 1

        while j <= right:
            tempArr[k] = self.arr[j]
            k += 1
            j += 1

        k = 0

        for i in range(left, right + 1):
            # Update the plot after each merge operation
            self.arr[i] = tempArr[k]
            k += 1

    def sort(self, left, right):
        if right > left:
            mid = (right + left) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.__merge(left, mid + 1, right)


class QuikSort(Sort):

    def __insertionSort(self, first, last):
        for i in range(first, last + 1):
            j = i
            while j > first:
                if self.arr[j - 1] > self.arr[j]:
                    (self.arr[j - 1], self.arr[j]) = (self.arr[j], self.arr[j - 1])
                    j -= 1
                    continue
                break

    def __medianOf3(self, first, middle, last):
        if self.arr[middle] < self.arr[first] < self.arr[last]:
            median = first
        elif self.arr[last] < self.arr[first] < self.arr[middle]:
            median = first
        elif self.arr[first] < self.arr[middle] < self.arr[last]:
            median = middle
        elif self.arr[last] < self.arr[middle] < self.arr[first]:
            median = middle
        else:
            median = last
        (self.arr[median], self.arr[last]) = (self.arr[last], self.arr[median])

    def __partition(self, first, last):
        x = self.arr[last]
        pInd = first - 1

        for j in range(first, last):
            if self.arr[j] <= x:
                pInd += 1
                self.arr[pInd], self.arr[j] = self.arr[j], self.arr[pInd]

        self.arr[pInd + 1], self.arr[last] = self.arr[last], self.arr[pInd + 1]
        return pInd + 1

    def sort(self, first, last):
        if first < last:
            if (last - first + 1) <= 3:
                self.__insertionSort(first, last)
            else:
                self.__medianOf3(first, (first + last) // 2, last)
                p = self.__partition(first, last)
                self.sort(first, p - 1)
                self.sort(p + 1, last)


class IntroSort(Sort):
    def __introSort(self, start, end, depth_limit):
        if end - start <= 1:
            return
        elif depth_limit == 0:
            self.__heapSort(start, end)
        else:
            p = self.__partition(start, end)
            self.sort(start, p + 1)
            self.sort(p + 1, end)

    def __partition(self, start, end):
        pivot = self.arr[start]
        i = start - 1
        j = end

        while True:
            i += 1
            while self.arr[i] < pivot:
                i += 1
            j -= 1
            while self.arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            self.arr[i], self.arr[j] = self.arr[j], self.arr[i]

    def __heapSort(self, start, end):
        def heapify(parent):
            child = 2 * parent + 1
            if child < end:
                if child + 1 < end and self.arr[child] < self.arr[child + 1]:
                    child += 1
                if self.arr[parent] < self.arr[child]:
                    self.arr[parent], self.arr[child] = self.arr[child], self.arr[parent]
                    heapify(child)

        for i in range(math.floor((end - start) / 2), -1, -1):
            heapify(i)
        for i in range(end - 1, start, -1):
            self.arr[start], self.arr[i] = self.arr[i], self.arr[start]
            heapify(start)

    def sort(self, start, end):
        depth_limit = 2 * math.floor(math.log(len(self.arr)))
        self.__introSort(start, end, depth_limit-1)