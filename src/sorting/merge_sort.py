


class MergeSort():

    @staticmethod
    def partition(arr):
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        return L , R


    @staticmethod
    def merge(arr, L, R):
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
    def solve(arr):
        if len(arr) > 1:
            L, R = MergeSort.partition(arr)
            MergeSort.solve(L)
            MergeSort.solve(R)
            MergeSort.merge(arr, L, R)


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]
        merge_sort(L)
        merge_sort(R)

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

