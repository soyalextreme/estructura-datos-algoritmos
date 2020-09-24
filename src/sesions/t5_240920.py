"""
Homework
Recursivity

Alejandro AS

"""
from lib.inputs import input_int



def sum_recursivity(n):
    """
    Sums n + n -1 until it is 1
    
    Alejandro AS

    """
    if n == 1:
        return 1
    return n + sum_recursivity(n - 1)


def sum_iterative(n):
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
        

def main():
    n = input_int("Give me a num: ")
    r_iterative = sum_iterative(n)
    r_recursion = sum_recursivity(n)
    print(f"recursion: {r_recursion}")
    print(f"iterative: {r_iterative}")
