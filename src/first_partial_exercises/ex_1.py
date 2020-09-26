

from lib.inputs import input_int

def n_tables(n):
    print("Lets Start!!")
    asserts = 0
    errors = 0
    for i in range(1, 11):
        user_try = input_int(f"{n} * {i} = ")

        if user_try == i * n:
            asserts += 1
            input("Correct! Congrats")
        else:
            errors += 1
    print(f"Assertions {asserts} Errors {errors}")
    if asserts == 10:
        print("Excellent Job buddy")
    elif asserts < 10 and asserts >= 8:
        print("Nice! you can improve")
    elif asserts < 8:
        print("Keep practicing you will get better")
        pass


def main():
    print("LEARN THE TABLES")
    print("="*40)
    n = input_int("What multiplication table you wanna learn:\n")
    if n == 0 or n == 1:
        print("What a easy challenge")
    elif n >= 12:
        print("Wow you the difficult challenges")
    
    n_tables(n)
