import random
from lib.inputs import input_int 
from lib.util import clean_screen



def print_matrix(m):
    """
        This function prints in format a matrix.

        @params:
            m => matrix to print in format

        Alejandro AS

    """
    for i in m:
        print("|", end=" ")
        for j in i:
            print("{n:>5} ".format(n = str(j)), end=" ")
        print("|")



def find_best_row(m):
    """
        This function finds the list | row that has more 0 in the matrix to
        make less calculus in the adjuct method.
        @params: 
            m => a matrix to find best row
        @return:
            res[0] => the number of the best row

        Alejandro AS
    """
    res = [0, 0] # [best_row, amount of 0]
    for i in range(len(m)):
        count = 0
        for j in range(len(m[i])):
            if m[i][j] == 0:
                count += 1
        if res[1] < count:
            res = [i, count]
    return res[0]


def reduce_matrix(m, best_row, col_ign):
    """
        This function reduces de matrix by adjuct law quiting a colum and
        a row.

        @params:
            m => matrix of n order
            best_row => the best row to ignore
            col_ign => the column to ignore
        @return:
            reduced_matrix => a matrix in n-1 order

        Alejandro AS

    """

    reduced_matrix = []
    for i in range(len(m)):
        if i == best_row:
            continue
        else:
            reduced_matrix.append([])
            for j in range(len(m[i])):
                if j != col_ign:
                    reduced_matrix[i - 1].append(m[i][j])
    return reduced_matrix



def transf_signs_rows(l, row):
    """
        This function calculates de sign assignment depending on the position
        of the number in the row of the matrix, checking the module of the sum
        of the row and the colum % 2. Reversing sign if the module is not 0.
        @params: l => list to reverse
                 row => number that represent the row in the matrix
        @return: l => formated values with the correct sign 

        Alejandro AS
    """
    for i  in range(len(l)):
        if (i + row) % 2 != 0:
            l[i] *= -1
    return l


def det(m):
    """ 
        Main Function that calculates de matrix implementing recursive by this
        function
        @paramas: m => array 2 dim
        @return: r => result of the determinat
        
        Alejandro AS
    """


    if len(m) == 2:
        return (m[0][0] *  m[1][1]) - (m[1][0] * m[0][1])


    # reduce the function until the matrix is 2 len
    # the best row to pick is the one wiht more 0
    best_row = 0

    l_trans = transf_signs_rows(m[best_row], best_row)
    l_red_m = []

    for i in range(len(l_trans)):
        l_red_m.append(reduce_matrix(m, best_row, i))

    # print(l_trans)
    # print(l_red_m)
    result = 0

    for i in range(len(l_trans)):
        result += l_trans[i] * det(l_red_m[i])
    return result
    

def gen_random_matrix(size):
    """ Randomly fiting the values of a matrix n """
    return [[ random.randint(-99, 99) for _ in range(size)] for _ in range(size)]


def create_matrix(size):
    """ Input for creating a matrix """
    m = []
    for i in range(size):
        m.append([])
        for j in range(size):
            n = input_int(f"Value row {i + 1} column {j + 1}: ", min_val= -99,
                         max_val=99, default=0)
            m[i].append(n)
    return m
        

def menu():
#    exp_n = [[3, 1, 17], [4, 13, -2], [1, -6 , -3]] #this should give you -772
#    r = det(exp_n)
#    print(r)
    RETURN_VAL = 4
    opc = 0

    while opc != RETURN_VAL:
        print("""
                DETERMINANT MATRIX
                1- A determinat of a matrix order 1 to 5 manually
                2- A determinat of a random matrix
                3- Show documentation.
                4- Go back
              """)
        opc = input_int("_")
        if opc == 1:
            size = input_int("Size of the matrix:",allow_negative=False, default=2, min_val=2, max_val=5)
            m = create_matrix(size)
            print_matrix(m)
            r = det(m)
            print(f"|m| = {r}")
            input("Enter to continue")
            clean_screen()
        if opc == 2:
            size = input_int("Size of the random matrix: ", min_val=2,
                             max_val=15, allow_negative=False,
                             default=2)
            m = gen_random_matrix(size)
            print_matrix(m)
            r = det(m)
            print(f"|m| = {r}")
            input("Enter to continue")
            clean_screen()
        if opc == 3:
            help(print_matrix)
            help(det)
            help(transf_signs_rows)
            help(reduce_matrix)
            clean_screen()
        if opc == 4:
            input("returning to main menu")
            clean_screen()
        else:
            clean_screen()




