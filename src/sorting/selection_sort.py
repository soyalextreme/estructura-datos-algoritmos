"""
    Selection Sort Algorithm

    22 - October - 2020
    Alejandro AS
"""
from sorting.sort import SortMethod


class SelectionSort(SortMethod):

    def __init__(self, l):
        """
            Constructor Method
            l => List to work with`
        """
        self.l = l
        self.l_sorted = l[:]
        SortMethod.__init__(self, self.l, self.l_sorted, "Selection Sort")
    
    def upward(self):
        """
            Selection Sort ascendent algorithm
            returns l_sorted
        """
        l = self.l_sorted
        n = len(l) 
        for i in range(n):
            low = i
            for j in range(i, n):
                if l[j] < l[low]:
                    low = j 
            l[low], l[i] = l[i], l[low]
        return l

    def downward(self):
        """
            Selection Sort descendent algorithm
            returns l_sorted
        """
        l = self.l_sorted
        n = len(l) 
        for i in range(n):
            high = i
            for j in range(i, n):
                if l[j] > l[high]:
                    high = j 
            l[high], l[i] = l[i], l[high]
        return l
