""" Here you can find util functions and clases to work the other files """


import os
import random
from constants import EXIT_VALUE


def clean_screen():
    """ Cleans the terminal depending on the operating system """
    try:
        if os.uname().sysname == "Windows":
            os.system("cls")
        os.system("clear")
    except:
        os.system("cls")


def exit():
    """ Function in charge of the exit process of the program
        Example delete temporary files as the graphs generated
    """
    os.system("rm __init__.html")
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
    return 0


def still_bool(msg="Wanna continue: [y/n]"):
    res = input(msg)
    if res.lower() == 'n':
        return False
    else:
        return True


def random_list(low=0, high=10, length=10):
    """ Function that creates a random list """
    return [random.randint(low, high) for _ in range(length)]
