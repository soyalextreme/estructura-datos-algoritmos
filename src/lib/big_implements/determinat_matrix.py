
import random

# def find_column(matix):
#     # [index | amount of 0]
#     op_row = [0, 0]
#     for i in range(len(matix)):
#         row_count_cero = 0
#         for j in range(len(matix[i])):
#             if matix[i][j] == 0:
#                 row_count_cero += 1
#         if op_row[1] < row_count_cero:
#             op_row = [i, row_count_cero]
#     return op_row[0]



# def reduce_matrix(matrix, column_ignore, row_ignore):
#     print_matrix(matrix)
#     if len(matrix) == 2:
#         print("Calculando primera parte")
#         return matrix[0][0] *  matrix[1][1] - matrix[1][0] * matrix[0][1]
#     reduced_matrix = []
#     n = 0
#     for i in range(len(matrix)):
#         if i == row_ignore:
#             continue
#         else:
#             reduced_matrix.append([])
#             for j in range(len(matrix[i])):
#                 if j == column_ignore:
#                     continue
#                 else:
#                     reduced_matrix[n].append(matrix[i][j])
#         n += 1
#     reduce_matrix(reduced_matrix, column_ignore, row_ignore)
#     return reduced_matrix 

                

# def det(a):
#     col_ignore = find_column(a)
#     print(col_ignore)
#     acum_matrix =  []
#     for i in range(len(a)):
#         matrix= reduce_matrix(a, i, col_ignore)
#         acum_matrix.append(matrix)
#     print(acum_matrix)

#     result = 0
#     for j in range(len(a[col_ignore])):
#         if ((col_ignore + 1) + (j + 1)) % 2 != 0:
#             a[col_ignore][j] *= -1
#         print(f"result = {a[col_ignore][j]} + {acum_matrix[j]}")
#         result = a[col_ignore][j] * reduce_matrix(acum_matrix[j], column_ignore=0, row_ignore=0)
#     print(a[col_ignore])
#     print(result)



    




# def gen_random_matrix(size):
#     return [[ random.randint(0, 9) for _ in range(size)] for _ in range(size)]

# def print_matrix(matrix):
#     print()
#     for i in matrix:
#         for j in i:
#             print(j, end=" ")
#         print()
#     print()


# if __name__ == "__main__":
#     # matrix_example = [[3, 1, 17],[4, 13, -2], [1,-6,-3]]
#     matrix_random = gen_random_matrix(5)

#     det(matrix_random)
    # det(matrix_example)



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
