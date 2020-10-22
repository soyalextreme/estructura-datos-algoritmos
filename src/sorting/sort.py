from lib.util import clean_screen


class SortMethod:

    def __init__(self, l, l_sorted, desc="Soting Algorithm"):
        self.l = l
        self.l_sorted = l_sorted
        self.desc = desc

    def print_results(self):
        clean_screen()
        print(self.desc.upper())
        print("Unsorted:")
        print(self.l)
        print("Sorted:")
        print(self.l_sorted)
        input("_")
