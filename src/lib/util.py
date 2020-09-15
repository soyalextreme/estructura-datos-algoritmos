""" Here you can find util functions and clases to work the other files """


import os
from lib.constants import EXIT_VALUE


def clean_screen():
    """ Cleans the terminal depending on the operating system """
    if os.uname().sysname == "Windows":
        os.system("cls")
    os.system("clear")


def exit():
    """ Function in charge of the exit process of the program
        Example delete temporary files as the graphs generated
    """
    print("Bye...")
 

def still():
    """ Checks the input o cancel de menu or no 
        Consider that in the main menu the opc that close cicle is 
        Number 5
    """
    print("*"*25)
    opc = input("Wanna continue: [y/n]")
    if opc == 'n':
        print("Good Bye... ")
        return EXIT_VALUE
    clean_screen()
    os.system("rm __init__.html")
    return 0   
