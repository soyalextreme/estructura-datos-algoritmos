""" Sesion 4 File 
    Date 15-09-20
    Alejandro Andrade Soriano
"""

import os
import random
from lib.inputs import input_int
from lib.util import clean_screen


def random_matrix_list():
    m = [ [random.randint(1, 100) for _ in range(random.randint(1, 30))] for _ in range(random.randint(0, 100))]

    for i in m:
        for j in i:
            print(j, end=" ")
        print()


    # tarea 
    # leer una matriz 
    # calcular su determinate
    # validar
    



def menu():
    EXIT_VAL = 4
    alumnos_del_profe_valdo = []
    opc = 0

    while opc != EXIT_VAL:
        print("MENU")
        print("1. Altas Alumnos")
        print("2. Reporte de Alumnos")
        print("3. Random Matrix List")
        print("4. Salir")
        opc = int(input_int("_"))
        if opc == 1:
            new_student = input("Name of the new student:\n")
            alumnos_del_profe_valdo.append(new_student)
            clean_screen()
        elif opc == 2:
            print("Alumnos:")
            for alum in alumnos_del_profe_valdo:
                print(alum)
            input("Enter to continue")
            clean_screen()
        elif opc == 3:
            random_matrix_list()
            input("Enter to continue")
            clean_screen()
        elif opc == EXIT_VAL:
            print("byeee.......")
            clean_screen()
        else:
            print("opc invalid")
            input("Enter to continue")
            clean_screen()



def main():
   menu() 
