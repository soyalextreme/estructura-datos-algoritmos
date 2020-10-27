


class HeapSort:

    @staticmethod
    def heapify(arr, n, i):
        largest = i
        l = i * 2 + 1 
        r = i * 2 + 2

        if l < n and arr[i] < arr[l]:
            largest = l

        if r < n and arr[largest] < arr[r]:
            largest = r
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            HeapSort.heapify(arr, n, largest)


    @staticmethod
    def solve(arr):
        n = len(arr)

        for i in range(n //2 -1 , -1, -1):
            HeapSort.heapify(arr, n, i)

        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            HeapSort.heapify(arr, i, 0)

import random
rand = [random.randint(1, 100) for _ in range(10000000)]
# print(rand)
HeapSort.solve(rand)
# print(rand)