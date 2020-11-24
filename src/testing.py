"""
    TESTING SCRIPTS
    Alejandro Andrade Soriano
    02/11/2020
"""


from sorting.bubble_sort import BubbleSort
from sorting.insertion_sort import InsertionSort
from sorting.selection_sort import SelectionSort
from sorting.shell_sort import ShellSort
from sorting.quick_sort import QuickSort
from sorting.merge_sort import MergeSort
from sorting.heap_sort import HeapSort

from sorting.bubble_sort_linked import BubbleSortLinked


from lib.util import random_list
from lib.inputs import input_int
from lib.decorators import cronometer
from lists.simple_linked_list import SimpleLinkedList
from lists.support_functions import LinkedList as LinkedListSup
from lib.util import clean_screen

# lists
from lists.simple_linked_list import SimpleLinkedList
from lists.double_linked_list import DoubleLinkedList


def test_sort(SortClass, linked=False):
    size = input_int("Size of the random List: ",
                     allow_negative=False, min_val=2)
    min_val = input_int("Min value to gen: ")
    max_val = input_int("Max value to gen: ")
    ascendent = input_int("0 = Ascendent\n1 = Descendent\nDefault = 0\n_",
                          allow_negative=False, max_val=1, min_val=0, default=0)

    if linked == False:
        l_ran = random_list(low=min_val, high=max_val, length=size)
    else:
        l = SimpleLinkedList()
        l_ran = LinkedListSup.fit_random(
            n_elements=size, l=l, low=min_val, high=max_val)

    s = SortClass(l_ran)

    @cronometer
    def timer():
        if ascendent == 1:
            s.downward()
        else:
            s.upward()

    print("Time to order: if the list is too large this should take a while")
    timer()
    print("FINISH!")
    input("_Enter to see the results")
    s.print_results()


def test_bubble_sort():
    test_sort(BubbleSort)


def test_quick_sort():
    test_sort(QuickSort)


def test_insertion_sort():
    test_sort(InsertionSort)


def test_selection_sort():
    test_sort(SelectionSort)


def test_shell_sort():
    test_sort(ShellSort)


def test_merge_sort():
    test_sort(MergeSort)


def test_heap_sort():
    test_sort(HeapSort)


"""
    SORTING METHODS WITH LINKED LISTS
"""


def test_bubble_sort_linked():
    test_sort(BubbleSortLinked, linked=True)


def comparison():
    print("Comparing n log n average complexity to n^2 complexity")
    print("In a list of 2500, 5000, 10000")
    rand_l_100 = random_list(-2500, 2500, 2500)
    rand_l_1000 = random_list(-5000, 5000, 5000)
    rand_l_2500 = random_list(-10000, 10000, 10000)
    test_1_q = QuickSort(rand_l_100)
    test_2_q = QuickSort(rand_l_1000)
    test_3_q = QuickSort(rand_l_2500)
    test_1_b = BubbleSort(rand_l_100)
    test_2_b = BubbleSort(rand_l_1000)
    test_3_b = BubbleSort(rand_l_2500)

    @cronometer
    def test_ob(obj):
        obj.upward()

    print("Quick sort Times")
    test_ob(test_1_q)
    test_ob(test_2_q)
    test_ob(test_3_q)

    print("Bubble sort Times")
    test_ob(test_1_b)
    test_ob(test_2_b)
    test_ob(test_3_b)


if __name__ == "__main__":
    clean_screen()
    l = DoubleLinkedList()
    LinkedListSup.fit_random(10, l, -10, 10)
    bl = BubbleSortLinked(l)
    order_list = bl.upward()
    bl.print_results()
    print(order_list.reverse())
