"""
    This file contians all the functions use for funcionality in the project 
    Alejandro AS
"""

from math import sqrt
import random


from lib.inputs import input_int, input_number_list
from lib.prints import print_title


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


def cuadratic_ecuations():
    """ Calculates x1, x2  in a cuadratic equation"""
    
    print_title("OPTION 2-CUADRATIC SOLUTIONS")
    a = input_int("Insert a number A in ecuation: ")
    b = input_int("Insert a number B in ecuation: ")
    c = input_int("Insert a number C in ecuation: ")
    try:
        x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
        x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
    except ValueError:
        x1 = (-b + sqrt(abs(b**2 - 4*a*c))) / (2 * a)
        x2 = (-b - sqrt(abs(b**2 - 4*a*c))) / (2 * a)
        return print(f"x1: {x1}i\nx2:{x2}i")
    except ZeroDivisionError:
        return print("We cant dive into 0.")
    print(f"x1: {x1}\nx2:{x2}")


def average_grades():
    """ Recibes inputs of grades and print the average """
    all_grades = []
    r = 0

    print_title("OPTION 3-AVERAGE GRADES")
    print("Advice: Not allowing negative numbers")
    all_grades = input_number_list(type="grade", allow_negative_num=False, max_n=10);
    # calculating
    for g in all_grades:
        r += g
    r  /= len(all_grades)
    print(all_grades)
    print(f"AVG OF GRADES: {r}")


def max_number():
    """ Returns max number of a list of numbers """
    print_title("OPTION 4-MAX NUMBER")
    all_n = input_number_list(type="number")
    max_n = all_n[0]
    for n in all_n:
        if n > max_n:
            max_n = n
    print(all_n)
    print(f"MAX NUMBER: {max_n}")


def max_random_num(size_list):
    """ Generates a random number list and finds the bigger 
        @params:
            size_list => integer that defines the size of the random list
        @return:
            tuple => max_number ordered_random_list
    """

    random_list = [random.randint(-500, 500) for _ in range(size_list) ]

    max_n = random_list[0]
    for n in random_list:
        if max_n < n:
            max_n = n
    print(random_list)
    print(f"The max number is: {max_n}")
    return random_list, max_n

