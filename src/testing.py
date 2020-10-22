from sorting.bubble_sort import BubbleSort
from lib.util import random_list
from time import sleep


def testing():
    l_ran = random_list()
    b = BubbleSort(l_ran)
    b.upward()
    b.print_results()
    b.downward()
    b.print_results()


testing()
