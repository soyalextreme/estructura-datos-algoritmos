"""
    Tarea Estructura de datos y algoritmos

    28 Septiembre del 2020
    SUMA DE DIGITOS DE UN NUMERO CON RECURSIVIDAD Y SIN CAST

    Alejandro AS.
"""
from lib.inputs import input_int
from lib.util import clean_screen


def sum_digits(num):
    """
        Sums all the digits of a integer number
    """
    if num // 10 == 0:
        return num
    return num % 10 + sum_digits(num // 10)


def main():
    """
        Main Handler function
    """
    clean_screen()
    num = input_int("Give me a Integer number to sum digits: ",
                    allow_negative=False)
    print(f"Num: {num}\n Sum Digits: {sum_digits(num)}")
