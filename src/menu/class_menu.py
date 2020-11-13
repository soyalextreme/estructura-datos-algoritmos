"""
    MAIN MENU CLASS
    Alejandro Andrade Soriano
    02/11/2020
"""

from lib.menu import Menu

from testing import test_bubble_sort, test_insertion_sort, test_selection_sort, test_shell_sort, test_quick_sort, test_heap_sort, test_merge_sort, comparison


def sorting_menu():
    m = Menu(SORTING_OPC, exit_val=9, welcome=False, still=True)
    m.start()


def init_menu():
    m = Menu(MAIN_OPC, exit_val=2, still=False,
             welcome=True, welcome_msg="Parcial 2\nESTRUCTURA DE DATOS\nALEJANDRO AS\n\nenter to continue")
    m.start()


MAIN_OPC = [(1, "Sorting Methods", sorting_menu), ]


SORTING_OPC = [(1, "Bubble Sort", test_bubble_sort),
               (2, "Insertion Sort", test_insertion_sort),
               (3, "Selection Sort", test_selection_sort),
               (4, "Shell Sort", test_shell_sort),
               (5, "Quick Sort", test_quick_sort),
               (6, "Merge Sort", test_merge_sort),
               (7, "Heap Sort", test_heap_sort),
               (8, "O(n Log n) vs O(n^2) comparison", comparison)
               ]
