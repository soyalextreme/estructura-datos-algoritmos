"""
    The init module for the exercise.
    This boots all the program.
"""
from lib.menu.epp_menu import Menu
from first_partial_exercises.options import MAIN_MENU 

def main():
    m = Menu(MAIN_MENU, welcome=True, exit_val=10)
    m.start()



