""" 
    Insertion Sort Algorithm

    ALejandro AS
    22 - October - 2020
"""
from sorting.sort import SortMethod
from lib.decorators import cronometer


class InsertionSort(SortMethod):

    def __init__(self, l):
        """
            Constructor Class 
            l => list to sort
        """
        self.l = l
        self.l_sorted = l[:]
        SortMethod.__init__(self, self.l, self.l_sorted, "Insertion Sort")

    def upward(self):
        """
            Sorting Method for ascendent
        """
        l = self.l_sorted
        for i in range(len(l)):
            j = i
            while j > 0 and l[j - 1] > l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
                j -= 1
        return l

        # Introduction to algorithms thomas cormel

    def downward(self):
        """
            Sorting Method for descendent
        """
        l = self.l_sorted
        for i in range(len(l)):
            j = i
            while j > 0 and l[j - 1] < l[j]:
                l[j], l[j - 1] = l[j - 1], l[j]
                j -= 1
        return l
