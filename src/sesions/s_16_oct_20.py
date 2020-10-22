"""
    Sesion 16 - October - 2020
"""
import random


def bubble_sort(l):
    for i in range(len(l)):
        changes = None
        for j in range(len(l) - 1):
            if l[j] > l[j + 1]:
                l[j], l[j + 1] = l[j + 1], l[j]
                changes = True
        if changes is None:
            break


def main():
    l = [random.randint(1, 20) for _ in range(10)]

    print(l)
    bubble_sort(l)
    print(l)


main()
