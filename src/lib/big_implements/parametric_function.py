import math
from lib.prints import print_table, draw_graph


def parametric_function(params, fx, fy, size, func_expresion):
    """ This function solves and calculetes n paramas constrains in fx and fy and then graphs this expressions in the plane"""
    x = []
    y = []
    for i in params:
        y_n = fy(i)
        x_n = fx(i) 
        x.append(x_n)
        y.append(y_n)
    
    print(func_expresion)
    print_table(x, y, params)
    draw_graph(x, y, size, "red")


def main():
    params_ex_1 = [0, math.pi/4, math.pi/2, (3*math.pi) /4, math.pi, (math.pi*5)/4, (math.pi*3)/2, (math.pi*7)/4, math.pi*2]
    def fx_ex_1(i):
        return 3*math.cos(i)
    def fy_ex_1(i):
        return 4*math.sin(i)

    params_ex_2 = [i for i in range(0, 9)]
    def fx_ex_2(i):
        return 1 / math.sqrt(i+1)
    def fy_ex_2(i):
        return i / (i + 1)


    parametric_function(params_ex_1, fx_ex_1, fy_ex_1, 0.05,
        func_expresion="f(x) = 3 Cos (θ)\nf(y) = 4 Sen (θ)\n"
    )
    print("\n"*4)
    parametric_function(params_ex_2, fx_ex_2, fy_ex_2, 0.006,
        func_expresion="f(x) = 1 / √θ+1 \nf(y) = θ / θ + 1\n"
    )

if __name__ == "__main__":
    main()
