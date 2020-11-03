"""
    Merge Sort Class Algorithm   
    Alejandro AS
    02/11/2020
"""

from sorting.sort import SortMethod


class MergeSort(SortMethod):

    def __init__(self, l):
        self.l = l
        self.l_sorted = l[:]
        SortMethod.__init__(self, l, self.l_sorted, "merge sort")

    def upward(self):
        MergeSort.partition(self.l_sorted, asc=True)

    def downward(self):
        MergeSort.partition(self.l_sorted, asc=False)

    @staticmethod
    def partition(arr, asc=True):
        if len(arr) > 1:
            mid = len(arr) // 2
            R = arr[:mid]
            L = arr[mid:]
            MergeSort.partition(R, asc)
            MergeSort.partition(L, asc)
            if asc is False:
                MergeSort.min_merge(arr, L, R)
            else:
                MergeSort.max_merge(arr, L, R)

    @staticmethod
    def max_merge(arr, L, R):
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    @staticmethod
    def min_merge(arr, L, R):
        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
