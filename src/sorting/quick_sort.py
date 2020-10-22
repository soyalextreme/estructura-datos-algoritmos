"""
    Quick Sort Algorithm

    Alejandro AS
    22-October-2020
"""
from sorting.sort import SortMethod



class QuickSort(SortMethod):

    def __init__(self, l):
        """ 
            Constructor Method 
            l => list of numbers
        """
        self.l = l
        self.l_sorted = l[:]
        SortMethod.__init__(self, self.l, self.l_sorted, "Quick Sort")

    def partition(self, low, high, asc=True):
        """
            Partition a list from the pivot
            low => low index of the sublist
            high => high max index of the sublist
            returns => index of the new pivot
        """
        l = self.l_sorted
        pivot = l[high]
        j = low - 1
        for i in range(low, high):
            if l[i] <= pivot and asc is True:
                j +=1
                l[j], l[i] = l[i], l[j]
            elif l[i] >= pivot and asc is False:
                j +=1
                l[j], l[i] = l[i], l[j]
        l[high], l[j + 1] = l[j + 1], l[high]
        return j + 1
            
    def upward(self, low=None, high=None):
        """
            Quick sort ascendent 
        """
        l = self.l_sorted
        if low is None and high is None:
            low = 0
            high = len(l) - 1

        if low < high:
            pivot = self.partition(low, high)
            self.upward(low, pivot - 1)
            self.upward(pivot + 1, high)

    def downward(self, low=None, high=None):
        """
            Quick sort descendent
        """
        l = self.l_sorted
        if low is None and high is None:
            low = 0
            high = len(l) - 1

        if low < high:
            pivot = self.partition(low, high, False)
            self.downward(low, pivot - 1)
            self.downward(pivot + 1, high)


