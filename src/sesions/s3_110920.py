
# module
import random
from lib.inputs import input_int


def random_higher_num(size_list):
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

        
if __name__ == "__main__":
    random_higher_num()
