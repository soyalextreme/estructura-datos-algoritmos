"""
    25-09-2020


    MENU CLASS FOR THE CONSOLE MENU
    Check the documentation in each function

    AUTHOR Alejandro Andrade Soriano
"""


from lib.inputs import input_int
from lib.util import clean_screen


def print_format_item(val, title):
    print(" {0:^5}  |  {1:^30}".format(val, title))



class Menu():
    __print_welcome = False
    __exit_val= 0
    __opc = 0
    __posible_options = [] 

    def __init__(self, opcs, exit_val, welcome=False):
        """
            Constructor of the class Menu
            Params:
                opcs => a list of tuples that contains the value of the opc,
                the title and the function
                welcome => a tag for the first time the proyect boots
                exit_val => the value that ends the program or returns
        """
        clean_screen()
        if welcome == True:
            self.print_welcome()
        self.__posible_options = opcs
        self.__exit_val = exit_val
        self.__welcome = welcome


    def print_opc(self):
        """
            This function prints all the posible options in the menu plus the
            exit val.

        """
        clean_screen()
        print("OPTIONS| PLEASE SELECT ONE")
        for item in self.__posible_options:
            print_format_item(item[0], item[1])
        print_format_item(self.__exit_val, f"{ 'Exit' if self.__welcome else 'Back' }")
        print("=" * 40)
        return input_int("_")


    def print_welcome(self):
        """
            This prints the welcome message for the first time the program
            boots.
        """
        print("WELCOME TO MY EXCERCISES")
        print("*"*20)
        print("Author: Alejandro AS")
        print("Estructura de datos y Algoritmos ")
        print("6to Semestre")
        input("Enter to continue")


    def eval_opc(self):
        """
            This option evals every option and in base of the current opc it
            excute a function of the opc.
        """
        for item in self.__posible_options:
            if self.__opc == self.__exit_val:
                # option if opc is equal to exit val
                self.exit()
                return 0
            elif item[0] == self.__opc:
                # executing the opc funct
                clean_screen()
                self.still(item[2])
                return 0
        print("WOUPS! select a posible option.")
        input()


    def still(self, func):
        """
            This function waits for a function to execute and then ends or not
            the program in base of a input.
        """
        def wrapper():
            func()
            still = input("Wanna continue [y/n]: ")
            if still.lower() == "n":
                self.__opc = self.__exit_val
                self.exit()
        wrapper()


    def exit(self):
        """
            The exit function for the menu
        """
        if self.__welcome:
            print("Bye...")
        else:
            print("Going to prev menu")


    def start(self):
        """
            The starter of the menu.
        """
        while self.__opc != self.__exit_val:
            self.__opc = self.print_opc()
            self.eval_opc()



    
    




    



