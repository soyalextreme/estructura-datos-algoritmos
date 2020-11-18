
from sorting.sort import SortMethod


class BubbleSortLinked(SortMethod):

    def __init__(self, linked_l):
        self.l = linked_l
        self.copy = self.l.copy()
        SortMethod.__init__(self, self.l, self.copy,
                            "Bubble sort with linked list")

    def upward(self):
        l = self.copy
        n = l.size()
        for i in range(n - 1):
            for j in range(n - i - 1):
                if l.get(j) > l.get(j + 1):
                    temp = l.get(j)
                    l.update(j, l.get(j + 1))
                    l.update(j + 1, temp)

    def downward(self):
        l = self.copy
        n = l.size()
        for i in range(n - 1):
            for j in range(n - i - 1):
                if l.get(j) < l.get(j + 1):
                    temp = l.get(j)
                    l.update(j, l.get(j + 1))
                    l.update(j + 1, temp)
