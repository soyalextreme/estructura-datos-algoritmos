""" Sesion 4 File 
    Date 15-09-20
    Alejandro Andrade Soriano
"""

import math
import os
from lib.inputs import input_int
from lib.util import clean_screen

def menu():
    EXIT_VAL = 3
    alumnos_del_profe_valdo = []
    opc = 0

    while opc != EXIT_VAL:
        print("MENU")
        print("1. Altas Alumnos")
        print("2. Reporte de Alumnos")
        print("3. Salir")
        opc = int(input_int("_"))
        if opc == 1:
            new_student = input("Name of the new student:\n")
            alumnos_del_profe_valdo.append(new_student)
            clean_screen()
        elif opc == 2:
            print(alumnos_del_profe_valdo)
            input("Enter to continue")
            clean_screen()
        elif opc == 3:
            print("byeee.......")
            clean_screen()
        else:
            print("opc invalid")
            input("Enter to continue")
            clean_screen()



def main():
   menu() 
