import heapq
import math
import random
import matplotlib.pyplot as plt


class Sort:
    def __init__(self, data):
        self._arr = data
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

    def _insertionSort(self, left, right):

        for i in range(left, right + 1):
            j = i
            while j > left:
                self._comp += 1

                if self._arr[j - 1] > self._arr[j]:
                    self._swap(j - 1, j)
                    j -= 1
                    continue
                break

    def _medianOf3(self, left, mid, right):

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

        i = left
        j = mid
        k = 0
        size = right - left + 1
        tempArr = [0] * size

        while (i < mid) and (j <= right):
            self._comp += 1
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

            self._arr[i] = tempArr[k]
            self._swaps += 1
            k += 1

    def sort(self, left, right):
        self._recursionDepth += 1

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth

        if right > left:
            mid = (right + left) // 2
            self.sort(left, mid)
            self.sort(mid + 1, right)
            self.__merge(left, mid + 1, right)

        self._recursionDepth -= 1


class QuikSort(Sort):

    def __partition(self, left, right):

        x = self._arr[right]
        pInd = left - 1

        for j in range(left, right):
            self._comp += 1
            if self._arr[j] <= x:
                pInd += 1
                self._swap(pInd, j)

        self._swap(pInd + 1, right)
        return pInd + 1

    def sort(self, left, right):

        self._recursionDepth += 1

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth

        if left < right:
            if (right - left + 1) <= 3:
                self._insertionSort(left, right)
            else:
                self._medianOf3(left, (left + right) // 2, right)
                p = self.__partition(left, right)
                self.sort(left, p - 1)
                self.sort(p + 1, right)

        self._recursionDepth -= 1


class IntroSort(Sort):
    def sort(self, left, right):
        max_depth = 2 * math.floor(math.log2(len(self._arr)))
        self.__introSort(self._arr, left, right, max_depth)

    def _partition(self, low, high):
        pivot = self._arr[high]
        p_index = low

        for i in range(low, high):
            self._comp += 1

            if self._arr[i] <= pivot:
                self._swap(i, p_index)
                p_index += 1

        self._swap(p_index, high)
        return p_index

    def _rand_partition(self, low, high):
        pivot_index = random.randint(low, high)
        self._swap(pivot_index, high)
        return self._partition(low, high)

    def _heapSort(self, begin, end):
        heapq.heapify(self._arr[begin:end + 1])
        for i in range(end, begin - 1, -1):
            self._swaps += 1
            self._arr[i] = heapq.heappop(self._arr[begin:end + 1])

    def __introSort(self, arr, begin, end, max_depth):

        self._recursionDepth += 1

        if self._recursionDepth > self._maxDepth:
            self._maxDepth = self._recursionDepth

        if end - begin < 16:
            self._insertionSort(begin, end)
        elif max_depth == 0:
            self._heapSort(begin, end)
        else:
            pivot = self._rand_partition(begin, end)
            self.__introSort(arr, begin, pivot - 1, max_depth - 1)
            self.__introSort(arr, pivot + 1, end, max_depth - 1)

        self._recursionDepth -= 1


def create_graph_merge_sort():
    sizes = [1000, 2500, 5000, 10000, 15000]
    merge_sort_ops = []
    merge_sort_ops2 = []

    for size in sizes:
        data = [random.randint(0, 1000) for _ in range(size)]

        merge_sort = MergeSort(data)
        merge_sort.sort(0, len(data) - 1)
        merge_sort_ops.append(merge_sort.NumOfOperations)
        merge_sort_ops2.append(merge_sort.NumOfOperations[3] * size)  # Get MaxDepth * size

    x = sizes
    y1 = [size * (math.log2(size)) for size in sizes]
    print(y1)
    y2 = [size * (math.log2(size)) for size in sizes]
    print(y2)
    y3 = merge_sort_ops2
    print(y3)

    plt.plot(x, y1, label="Dependency 1: Line = n * log2 n")
    plt.plot(x, y2, label="Dependency 2: Line = n * log2 n")
    plt.plot(x, y3, label="Dependency 3: Line = MaxDepth * n")
    plt.xlabel("Array Size")
    plt.ylabel("Number of Operations")
    plt.title("Merge Sort Performance")
    plt.legend()
    plt.show()


def create_graph_quick_sort():
    sizes = [1000, 2500, 5000, 10000, 15000]
    sort_ops = []
    sort_ops2 = []

    for size in sizes:
        data = [random.randint(0, 1000) for _ in range(size)]

        _sort = QuikSort(data)
        _sort.sort(0, len(data) - 1)
        sort_ops.append(_sort.NumOfOperations)
        sort_ops2.append(_sort.NumOfOperations[3] * size)  # Get MaxDepth * size

    x = sizes
    y1 = [size * (math.log2(size)) for size in sizes]
    print(y1)
    y2 = [size * (math.log2(size)) for size in sizes]
    print(y2)
    y3 = sort_ops2
    print(y3)

    plt.plot(x, y1, label="Dependency 1: Line = n * log2 n")
    plt.plot(x, y2, label="Dependency 2: Line = n * n")
    plt.plot(x, y3, label="Dependency 3: Line = MaxDepth * n")
    plt.xlabel("Array Size")
    plt.ylabel("Number of Operations")
    plt.title("Quik Sort Performance")
    plt.legend()
    plt.show()


def create_graph_intro_sort():
    sizes = [1000, 2500, 5000, 10000, 15000]
    sort_ops = []
    sort_ops2 = []

    for size in sizes:
        data = [random.randint(0, 1000) for _ in range(size)]

        _sort = IntroSort(data)
        _sort.sort(0, len(data) - 1)
        sort_ops.append(_sort.NumOfOperations)
        sort_ops2.append(_sort.NumOfOperations[3] * size)  # Get MaxDepth * size

    x = sizes
    y1 = [size * (math.log2(size)) for size in sizes]
    print(y1)
    y2 = [size * (math.log2(size)) for size in sizes]
    print(y2)
    y3 = sort_ops2
    print(y3)

    plt.plot(x, y1, label="Dependency 1: Line = n * log2 n")
    plt.plot(x, y2, label="Dependency 2: Line = n * log2 n")
    plt.plot(x, y3, label="Dependency 3: Line = MaxDepth * n")
    plt.xlabel("Array Size")
    plt.ylabel("Number of Operations")
    plt.title("Intro Sort Performance")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    create_graph_merge_sort()
    # create_graph_quick_sort()
    # create_graph_intro_sort()
