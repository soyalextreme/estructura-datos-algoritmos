"""
Homework
Recursivity

Alejandro AS

"""
from lib.inputs import input_int
from lib.util import clean_screen
from lib.decorators import cronometer


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


def fibonacci(n, memo=[]):
    if len(memo) == 0:
        memo = [None for _ in range(n)]
    if n == 1:
        return 1
    elif n == 0:
        return 0
    if memo[n - 1] is None:
        memo[n - 1] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n - 1]


def fibonacci_slow(n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fibonacci_slow(n - 1) + fibonacci_slow(n - 2)


def main():
    clean_screen()
    n = input_int("Give me a num: ")
    r_iterative = iterative_sum(n)
    r_recursion = recursive_sum(n)

    @cronometer
    def conatiner_fibo(n):
        print(f"Fibo with memo: {fibonacci(n)}")

    @cronometer
    def container_fibo_slow(n):
        print(f"Fibo SLOOOOW: {fibonacci_slow(n)}")

    conatiner_fibo(n)
    container_fibo_slow(n)
    print(f"factorial: {factorial(n)}")
    print(f"recursion: {r_recursion}")
    print(f"iterative: {r_iterative}")
