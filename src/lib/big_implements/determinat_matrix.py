
import random


def print_matrix(m):
    for i in m:
        print("|", end=" ")
        for j in i:
            print("{n:>3} ".format(n = str(j)), end=" ")
        print("|")
    print()



def find_best_row(m):
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
    for i  in range(len(l)):
        if (i + row) % 2 != 0:
            l[i] *= -1
    return l


def det(m):
    # print_matrix(m)
    if len(m) == 2:
        return (m[0][0] *  m[1][1]) - (m[1][0] * m[0][1])


    # reduce the function until the matrix is 2 len
    # the best row to pick is the one wiht more 0
    best_row = 0

    l_trans = transf_signs_rows(m[best_row], best_row)
    l_red_m = []
    # print(l_trans)

    for i in range(len(l_trans)):
        l_red_m.append(reduce_matrix(m, best_row, i))

    
    # print(l_trans)
    # print(l_red_m)
    result = 0

    for i in range(len(l_trans)):
        result += l_trans[i] * det(l_red_m[i])
    return result
    

def gen_random_matrix(size):
    return [[ random.randint(0, 20) for _ in range(size)] for _ in range(size)]


if __name__ == "__main__":
    exp_m = [[2, 3], [3, 2]]
    exp_n = [[1, 2, 3], [1, 0, 3], [1, 2 , 3]]
    exp_n = [[3, 1, 17], [4, 13, -2], [1, -6 , -3]]
    exp_n = gen_random_matrix(2)
    result = det(exp_n)
    print_matrix(exp_n)
    print(f"|a| = {result}")
