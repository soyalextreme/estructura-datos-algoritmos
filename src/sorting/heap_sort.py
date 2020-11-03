""" 
    Heap sort class Algorithm 
    02/11/2020
    Alejandro AS
"""
from sorting.sort import SortMethod


class HeapSort(SortMethod):

    def __init__(self, l):
        """
            L => List of real numbers
        """
        self.l = l
        self.l_sorted = l[:]
        SortMethod.__init__(self, l, self.l_sorted, "Heap Sort")

    def upward(self):
        l = self.l_sorted
        n = len(l)

        # build heap
        for i in range(n//2 - 1, -1, -1):
            HeapSort.max_heapify(l, n, i)

        for j in range(n - 1, 0, -1):
            # swap values
            l[0], l[j] = l[j], l[0]
            HeapSort.max_heapify(l, j, 0)

    def downward(self):
        l = self.l_sorted
        n = len(l)
        # build heap
        for i in range(n//2 - 1, -1, -1):
            HeapSort.min_heapify(l, n, i)

        for j in range(n - 1, 0, -1):
            # swap values
            l[0], l[j] = l[j], l[0]
            HeapSort.min_heapify(l, j, 0)

    @staticmethod
    def min_heapify(arr, n, i):
        minimun = i
        L = i * 2 + 1
        R = i * 2 + 2

        if L < n and arr[L] < arr[i]:
            minimun = L

        if R < n and arr[R] < arr[minimun]:
            minimun = R

        if i != minimun:
            arr[minimun], arr[i] = arr[i], arr[minimun]
            HeapSort.min_heapify(arr, n, minimun)

    @staticmethod
    def max_heapify(arr, n, i):
        maximum = i
        L = i * 2 + 1
        R = i * 2 + 2

        if L < n and arr[L] > arr[i]:
            maximum = L

        if R < n and arr[R] > arr[maximum]:
            maximum = R

        if maximum != i:
            arr[i], arr[maximum] = arr[maximum], arr[i]
            HeapSort.max_heapify(arr, n, maximum)
