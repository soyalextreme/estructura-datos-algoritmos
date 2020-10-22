from sorting.bubble_sort import BubbleSort
from sorting.insertion_sort import InsertionSort
from sorting.selection_sort import SelectionSort
from sorting.shell_sort import ShellSort
from sorting.quick_sort import QuickSort
from lib.util import random_list
from lib.inputs import input_int
from lib.decorators import cronometer

def testing_bubble_sort():
    l_ran = random_list()
    b = BubbleSort(l_ran)
    b.upward()
    b.print_results()
    b.downward()
    b.print_results()


def testing_insertion_sort():
    l_ran = random_list()
    i = InsertionSort(l_ran)
    i.upward()
    i.print_results()
    i.downward()
    i.print_results()

def testing_selection_sort():
    l_ran = random_list()
    s = SelectionSort(l_ran)
    s.upward()
    s.print_results()
    s.downward()
    s.print_results()

def test_shell_sort():
    l_ran = random_list()
    s = ShellSort(l_ran)
    s.upward()
    s.print_results()
    s.downward()
    s.print_results()

def test_quick_sort():
    size = input_int("Size of the random List: ", allow_negative=False, min_val=2)
    min_val = input_int("Min value to gen: ")
    max_val = input_int("Max value to gen: ")
    l_ran = random_list(low=min_val, high=max_val, length=size)
    q = QuickSort(l_ran)
    q.upward()
    q.print_results()
    q.downward()
    q.print_results()


def comparison():
    print("Comparing nlogn average complexity to n^2 complexity")
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
    comparison() 