from lib.util import clean_screen


class SortMethod:

    def __init__(self, l, l_sorted, desc="Sorting Algorithm"):
        self.l = l
        self.l_sorted = l_sorted
        self.desc = desc

    def print_results(self):
        clean_screen()
        string_chain = f"{self.desc.upper()}\nUnsorted:\n{self.l}\nSorted:\n{self.l_sorted}"
        input(string_chain)
