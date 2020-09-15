""" File in charge of the main menu Logic and manage the selctions """

from lib.inputs import input_int
from lib.prints import print_title
from lib.util import exit, still, clean_screen
from lib.constants import EXIT_VALUE
from lib.implements import triangle_area, cuadratic_ecuations, average_grades, max_number, max_random_num 
from lib.big_implements.parametric_function import main as parametric_function
from lib.big_implements.cyclode_function import main as cyclode_function


def main_menu():
    """ Main menu function program"""  
    clean_screen()
    opc = 0
    while opc != EXIT_VALUE:
        print(""" 
        MAIN MENU
        ***************************************
        1. Triangle Area
        2. Solution Cuadratic Equations 
        3. Average of n Grades 
        4. Higher value of n Numbers
        5. Hiegher value of random Numbers
        6. Parametric Functions - Vector Calculation
        7. Cycloid Funcitions - Vector Calculation
        8. Exit
        """)

        # Input
        opc = input_int("_")

        # Main Options
        if opc == 1:
            triangle_area()
            opc = still()
        elif opc == 2:
            cuadratic_ecuations()
            opc = still()
        elif opc == 3:
            average_grades()
            opc = still()
        elif opc == 4:
            max_number()
            opc = still()
        elif opc == 5:
            print_title("OPTION 5 - Higher num of random numbers")
            size = input_int("Tamano de la lista: ")
            max_random_num(size)
            opc = still()
        elif opc == 6:
            parametric_function()
            opc = still() 
        elif opc == 7:
            cyclode_function()
            opc = still()
        elif opc == EXIT_VALUE:
            exit()
        else:
            print("Option No valid Check de menu")
        

