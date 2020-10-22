"""
    Bubble Sorting Algorithm

    Alejandro AS
    22 / October / 2020
"""

import random
from sorting.sort import SortMethod


class BubbleSort(SortMethod):

    def __init__(self, l):
        """
            Constructor Method
        """
        self.l = l
        self.l_sorted = self.l[:]
        SortMethod.__init__(self, l, self.l_sorted, "bubble sort")

    def upward(self):
        """
            Ascendent Order
        """
        l_sorted = self.l_sorted
        for i in range(len(l_sorted)):
            changes = False
            for j in range(len(l_sorted) - i - 1):
                if l_sorted[j] > l_sorted[j + 1]:
                    l_sorted[j + 1], l_sorted[j] = l_sorted[j], l_sorted[j + 1]
                    changes = True
            if changes is False:
                break
        return l_sorted

    def downward(self):
        """
            Descendent Order
        """
        l_sorted = self.l_sorted
        for i in range(len(l_sorted)):
            changes = False
            for j in range(len(l_sorted) - i - 1):
                if l_sorted[j] < l_sorted[j + 1]:
                    l_sorted[j + 1], l_sorted[j] = l_sorted[j], l_sorted[j + 1]
                    changes = True
            if changes is False:
                break
        return l_sorted
