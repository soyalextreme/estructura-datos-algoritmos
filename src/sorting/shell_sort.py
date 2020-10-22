"""
    Shell Sorting Recursive Algorithm

    Alejandro AS
    22 - October - 2020
"""
from sorting.sort import SortMethod


class ShellSort(SortMethod):

    def __init__(self, l):
        """
            Constructor Class
            l => List of numbers to sort
        """
        self.l = l
        self.l_sorted = l[:]
        SortMethod.__init__(self, self.l, self.l_sorted,"Shell Sort Algorithm")
    

    def upward(self, gap=-1):
        """ 
            Ascendent Sorting Algorithm
        """
        l = self.l_sorted
        n = len(l)
        if gap == -1:
            gap = len(l) // 2
        elif gap == 0:
            return l
        else:
            gap //= 2

        for i in range(gap, n):
            j = i
            while j > 0 and l[j] < l[j - gap]:
                l[j], l[j - gap] = l[j - gap], l[j]
                j -= 1
        
        return self.upward(gap)


    def downward(self, gap=-1):
        """
            Descendent Sorting Algorithm
        """
        l = self.l_sorted
        n = len(l)
        if gap == -1:
            gap = len(l) // 2
        elif gap == 0:
            return l
        else:
            gap //= 2
        for i in range(gap, n):
            j = i
            while j > 0 and l[j] > l[j - gap]:
                l[j], l[j - gap] = l[j - gap], l[j]
                j -= 1
        
        return self.downward(gap)


