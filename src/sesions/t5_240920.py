"""
Homework
Recursivity

Alejandro AS

"""
from lib.inputs import input_int
from lib.util import clean_screen



def recursive_sum(n):
    """
    Sums n + n -1 until it is 1
    Alejandro AS
    """
    if n == 1:
        return 1
    return n + recursive_sum(n - 1)


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


def iterative_sum(n):
    """
    Sums a number from 1 to n.
    n = 2 => 1 + 2 
    return
    
    Alejandro AS
    """
    r = 0
    for i in range(1, n + 1):
        r += i 
    return r

def fibonacci(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibonacci(n -1) + fibonacci(n - 2)

# programa que lea un numero entero
# separar los digitos
# luego resultado
# sin cast de string

        

def main():
    clean_screen()
    n = input_int("Give me a num: ")
    #r_iterative = iterative_sum(n)
    #r_recursion = recursive_sum(n)  
    print(f"Fibo: {fibonacci(n)}")
    #print(f"factorial: {factorial(n)}")
    #print(f"recursion: {r_recursion}")
    #print(f"iterative: {r_iterative}")
