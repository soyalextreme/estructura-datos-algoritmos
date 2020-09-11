from math import sqrt
# own lib
from lib.inputs import input_int, input_number_list as input_list, print_title


def still():
    """ Checks the input o cancel de menu or no 
        Consider that in the main menu the opc that close cicle is 
        Number 5
    """
    print("*"*25)
    opc = input("Wanna continue: [y/n]")
    if opc == 'n':
        print("Good Bye... ")
        return 5
    return 0


def cuadratic_ecuations():
    """ Calculates x1, x2  in a cuadratic equation"""
    print_title("OPTION 2-CUADRATIC SOLUTIONS")
    a = input_int("Insert a number A in ecuation: ")
    b = input_int("Insert a number B in ecuation: ")
    c = input_int("Insert a number C in ecuation: ")
    # if(a <= 0):
    #     print("No cero div")
    #     return 0, 0
    try:
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    except ValueError:
        print("Working with imaginary numbers.")
        return 0, 0
    except ZeroDivisionError:
        print("We cant dive into 0.")
    print(f"x1: {x1}\nx2:{x2}")


def triangle_area():
    """ Calculate and prints the area of a triangle""" 
    print_title("OPTION 1-TRIANGLE AREA")
    h = input_int("Triangle height: ")
    b = input_int("Triangle base: ")
    precision = input("Do you want Decimals?: [y/n]")
    if precision == "y":
       r = (b * h) / 2
    else:
        r = (b * h) // 2
    print(f"AREA: {r}")


def average_grades():
    """ Recibes inputs of grades and print the average """
    all_grades = []
    still = "" 
    r = 0

    print_title("OPTION 3-AVERAGE GRADES")
    all_grades = input_list(type="grade");
    # calculating
    for g in all_grades:
        r += g
    r  /= len(all_grades)
    print(all_grades)
    print(f"AVG OF GRADES: {r}")


def max_number():
    """ Returns max number of a list of numbers """
    print_title("OPTION 4-MAX NUMBER")
    all_n = input_list(type="number")
    max_n = all_n[0]
    for n in all_n:
        if n > max_n:
            max_n = n
    print(all_n)
    print(f"MAX NUMBER: {max_n}")
    

def menu():
    """ Main menu function """  
    opc = 0
    while int(opc) != 5:
        print(""" 
        MAIN MENU
        ***************************************
        1. Triangle Area
        2. Solution Cuadratic Equations 
        3. Average of n Grades 
        4. Higher value of n Numbers
        5. Salir
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
        elif int(opc) == 5:
            print("Good Bye..")
        else:
            print("Option No valid Check de menu")


if __name__ == "__main__":
    menu()
 
