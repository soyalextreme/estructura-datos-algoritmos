"""
    Sesion 7
    29 - 09 -20

    Alejandro Andrade Soriano
"""

from lib.util import clean_screen
from time import sleep
from lib.inputs import input_int
from lib.decorators import cronometer


def pascal(j, i):
    if i == j or i == 1:
        return 1
    return pascal(j - 1, i - 1) + pascal(j - 1, i)


def draw_triangle(n, m=[]):

    # dibujo
    def draw():
        clean_screen()
        for column in m:
            for item in column:
                print(f"| {item} |", end="")
            print()
        sleep(0.5)

    # generar
    for j in range(n):
        m.append([])
        for i in range(j + 1):
            if i == 0 or j == i:
                m[j].append(1)
                draw()
                continue
            m[j].append(m[j - 1][i] + m[j-1][i-1])
            draw()


@cronometer
def main():
    clean_screen()
    row = input_int("Row of the digit to search: ", False)
    column = input_int("Column of the digit to search: ", False, max_val=row)
    r = pascal(row, column)  # 6
    input(f"the digit in position [{row},{column}] is {r}")
    draw_triangle(row)
