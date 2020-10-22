from sorting.bubble_sort import BubbleSort
from sorting.insertion_sort import InsertionSort
from lib.util import random_list
from time import sleep


def testing_bubblesort():
    l_ran = random_list()
    b = BubbleSort(l_ran)
    b.upward()
    b.print_results()
    b.downward()
    b.print_results()


def testing_insertionsort():
    l_ran = random_list()
    i = InsertionSort(l_ran)
    i.upward()
    i.print_results()
    i.downward()
    i.print_results()



if __name__ == "__main__":
    testing_insertionsort()
    