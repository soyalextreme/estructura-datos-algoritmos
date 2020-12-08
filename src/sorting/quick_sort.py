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
                j += 1
                l[j], l[i] = l[i], l[j]
            elif l[i] >= pivot and asc is False:
                j += 1
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


class QuickSortDoctorName():

    def __init__(self, l):
        """ 
            Constructor Method 
            l => list of numbers
        """
        self.l = l
        self.l_sorted = l.copy()

    def partition(self, low, high, asc=True):
        """
            Partition a list from the pivot
            low => low index of the sublist
            high => high max index of the sublist
            returns => index of the new pivot
        """
        l = self.l_sorted
        pivot = l.get(high).get_doctor().get_full_name()
        j = low - 1
        for i in range(low, high):
            if l.get(i).get_doctor().get_full_name() <= pivot and asc is True:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
            elif l.get(i).get_doctor().get_full_name() >= pivot and asc is False:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
        temp = l.get(high)
        l.update(l.get(j + 1), high)
        l.update(temp, j + 1)
        # l[high], l[j + 1] = l[j + 1], l[high]
        return j + 1

    def upward(self, low=None, high=None):
        """
            Quick sort ascendent 
        """
        l = self.l_sorted
        if low is None and high is None:
            low = 0
            high = l.size() - 1

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
            high = l.size() - 1

        if low < high:
            pivot = self.partition(low, high, False)
            self.downward(low, pivot - 1)
            self.downward(pivot + 1, high)

    def get_sorted(self):
        return self.l_sorted


class QuickSortPatientName():

    def __init__(self, l):
        """ 
            Constructor Method 
            l => list of numbers
        """
        self.l = l
        self.l_sorted = l.copy()

    def partition(self, low, high, asc=True):
        """
            Partition a list from the pivot
            low => low index of the sublist
            high => high max index of the sublist
            returns => index of the new pivot
        """
        l = self.l_sorted
        pivot = l.get(high).get_patient().get_full_name()
        j = low - 1
        for i in range(low, high):
            if l.get(i).get_patient().get_full_name() <= pivot and asc is True:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
            elif l.get(i).get_patient().get_full_name() >= pivot and asc is False:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
        temp = l.get(high)
        l.update(l.get(j + 1), high)
        l.update(temp, j + 1)
        # l[high], l[j + 1] = l[j + 1], l[high]
        return j + 1

    def upward(self, low=None, high=None):
        """
            Quick sort ascendent 
        """
        l = self.l_sorted
        if low is None and high is None:
            low = 0
            high = l.size() - 1

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
            high = l.size() - 1

        if low < high:
            pivot = self.partition(low, high, False)
            self.downward(low, pivot - 1)
            self.downward(pivot + 1, high)

    def get_sorted(self):
        return self.l_sorted


class QuickSortPatientAge():

    def __init__(self, l):
        """ 
            Constructor Method 
            l => list of numbers
        """
        self.l = l
        self.l_sorted = l.copy()

    def partition(self, low, high, asc=True):
        """
            Partition a list from the pivot
            low => low index of the sublist
            high => high max index of the sublist
            returns => index of the new pivot
        """
        l = self.l_sorted
        pivot = l.get(high).get_patient().get_age()
        j = low - 1
        for i in range(low, high):
            if l.get(i).get_patient().get_age() <= pivot and asc is True:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
            elif l.get(i).get_patient().get_age() >= pivot and asc is False:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
        temp = l.get(high)
        l.update(l.get(j + 1), high)
        l.update(temp, j + 1)
        # l[high], l[j + 1] = l[j + 1], l[high]
        return j + 1

    def upward(self, low=None, high=None):
        """
            Quick sort ascendent 
        """
        l = self.l_sorted
        if low is None and high is None:
            low = 0
            high = l.size() - 1

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
            high = l.size() - 1

        if low < high:
            pivot = self.partition(low, high, False)
            self.downward(low, pivot - 1)
            self.downward(pivot + 1, high)

    def get_sorted(self):
        return self.l_sorted


class QuickSortDoctorAge():

    def __init__(self, l):
        """ 
            Constructor Method 
            l => list of numbers
        """
        self.l = l
        self.l_sorted = l.copy()

    def partition(self, low, high, asc=True):
        """
            Partition a list from the pivot
            low => low index of the sublist
            high => high max index of the sublist
            returns => index of the new pivot
        """
        l = self.l_sorted
        pivot = l.get(high).get_doctor().get_age()
        j = low - 1
        for i in range(low, high):
            if l.get(i).get_doctor().get_age() <= pivot and asc is True:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
            elif l.get(i).get_doctor().get_age() >= pivot and asc is False:
                j += 1
                temp = l.get(i)
                l.update(l.get(j), i)
                l.update(temp, j)
                # l[j], l[i] = l[i], l[j]
        temp = l.get(high)
        l.update(l.get(j + 1), high)
        l.update(temp, j + 1)
        # l[high], l[j + 1] = l[j + 1], l[high]
        return j + 1

    def upward(self, low=None, high=None):
        """
            Quick sort ascendent 
        """
        l = self.l_sorted
        if low is None and high is None:
            low = 0
            high = l.size() - 1

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
            high = l.size() - 1

        if low < high:
            pivot = self.partition(low, high, False)
            self.downward(low, pivot - 1)
            self.downward(pivot + 1, high)

    def get_sorted(self):
        return self.l_sorted
