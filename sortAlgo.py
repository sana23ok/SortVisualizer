import math
#  методи
#       a)	швидкого сортування;
#       b)  інтроспективне сортування;
#       c)  сортування злиттям (Д. фон Неймана);


#-----------INTRO SORT--------------
def introSort(arr, start, end, depth_limit):
    if end - start <= 1:
        return
    elif depth_limit == 0:
        heapSort(arr, start, end)
    else:
        p = partitionIntro(arr, start, end)
        introSort(arr, start, p + 1, depth_limit - 1)
        introSort(arr, p + 1, end, depth_limit - 1)


def partitionIntro(arr, start, end):
    pivot = arr[start]
    i = start - 1
    j = end

    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


def heapSort(arr, start, end):

    def heapify(parent):
        child = 2 * parent + 1
        if child < end:
            if child + 1 < end and arr[child] < arr[child + 1]:
                child += 1
            if arr[parent] < arr[child]:
                arr[parent], arr[child] = arr[child], arr[parent]
                heapify(child)

    for i in range(math.floor((end - start) / 2), -1, -1):
        heapify(i)
    for i in range(end - 1, start, -1):
        arr[start], arr[i] = arr[i], arr[start]
        heapify(start)


#-----------QUICK SORT--------------
def quickSort(A, first, last):
    if first < last:
        if (last - first + 1) <= 3:
            insertionSort(A, first, last)
        else:
            medianOf3(A, first, (first + last) // 2, last)
            p = partition(A, first, last)
            quickSort(A, first, p - 1)
            quickSort(A, p + 1, last)


def insertionSort(A, first, last):
    for i in range(first, last+1):
        j = i
        while j > first:
            if A[j - 1] > A[j]:
                (A[j - 1], A[j]) = (A[j], A[j - 1])
                j -= 1
                continue
            break


def medianOf3(A, first, middle, last):
    if A[middle] < A[first] < A[last]:
        median = first
    elif A[last] < A[first] < A[middle]:
        median = first
    elif A[first] < A[middle] < A[last]:
        median = middle
    elif A[last] < A[middle] < A[first]:
        median = middle
    else:
        median = last
    (A[median], A[last]) = (A[last], A[median])


def partition(A, first, last):
    x = A[last]
    pInd = first-1

    for j in range(first, last):
        if A[j] <= x:
            pInd += 1
            A[pInd], A[j] = A[j], A[pInd]

    A[pInd+1], A[last] = A[last], A[pInd+1]
    return pInd+1


#-----------MERGE SORT--------------
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


class Sort:
    arr = [15, 45, 47, 1, 2, 5, 77, 6, 25, 333, -84, -4, -44]
    choice = None

    def __init__(self, choice):
        self.choice = choice

    # if choice == 1:
    # mergeSort(arr, 0, len(arr)-1)
    # elif choice == 2:
    #quickSort(arr, 0, len(arr)-1)
    introSort(arr, 0, len(arr), 2 * math.log(len(arr)))

    def print(self):
        print(f"Sorted arr = {self.arr}")


obj1 = Sort(2)
obj1.print()
