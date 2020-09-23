import math
from lib.prints import print_table, draw_graph, draw_multiple_graphs


def pf_decorator(function):
    def wrapper():
        x = []
        y = []
        x_fun, y_fun, params = function()

        for t in params:
            x.append(x_fun(t))
            y.append(y_fun(t))
        print_table(x, y, params)
        draw_graph(x, y, 0.005, "red")
        return x, y
    return wrapper





def parametric_function(params, fx, fy, size, func_expresion,
                        tangent=None, mx=None, function_my=None):
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
    if tangent is None:
        draw_graph(x, y, size, "red")
        return 0

    my = []
    for x in mx:
        # calculation the "y" tangent values
        my_n = function_my(x)
        my.append(my_n)
        
 
    graph = [[x, y], [mx, my]]

    draw_multiple_graphs(graph, size, "red")
    




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


    params_ex_3 = [n for n in range(-6, 6)]

    def fx_ex_3(i):
        return math.pow(i, 2) - 4

    def fy_ex_3(i):
        return math.pow(i, 3) - (3 * i)


    params_ex_4 = [n for n in range(-15, 16)]

    def fx_ex_4(i):
        return 2 * i - math.pi * math.sin(i)

    
    def fy_ex_4(i):
        return 2 - math.pi * math.cos(i)

    def fym_ex_4(x):
        m = -7.8546
        return m * x + 1.44


    parametric_function(params_ex_1, fx_ex_1, fy_ex_1, 0.05,
        func_expresion="f(x) = 3 Cos (θ)\nf(y) = 4 Sen (θ)\n"
    )
    print("\n"*4)
    parametric_function(params_ex_2, fx_ex_2, fy_ex_2, 0.006,
        func_expresion="f(x) = 1 / √θ+1 \nf(y) = θ / θ + 1\n"
    )
    print("\n"*4)
    parametric_function(params_ex_3, fx_ex_3, fy_ex_3, 0.05,
                        func_expresion="f(x) = t^2 - 4\nf(y) = t^3 -3t")


    print("\n")
    parametric_function(params_ex_4, fx_ex_4, fy_ex_4, 0.005,
                        func_expresion="f(x) = 2t - pi sen t \n f(y) = 2 - pi cos t")

if __name__ == "__main__":
    main()
