import random


class LinkedList():

    @staticmethod
    def fit_random(n_elements, l, low=0, high=10):
        # exception if the low is min introduced by the user
        if low > high:
            low, high = high, low

        for _ in range(n_elements):
            l.append(random.randint(low, high))
        return l
