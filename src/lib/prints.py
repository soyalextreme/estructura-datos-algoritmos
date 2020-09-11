def print_table(x, y, parameter):
    op = 0
    while op < len(parameter):
        print("*"*104)
        if op == 0:
            print("* {0:^30}  |  {1:^30}  |  {2:^30} *".format("Parameter", "x",  "y"))
            print("*"*104)
        print("* {0:^30}  |  {1:^30}  |  {2:^30} *".format(parameter[op], x[op],  y[op]))
        print("*"*104)
        op += 1