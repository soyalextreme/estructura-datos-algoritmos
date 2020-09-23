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


def pft_decorator(function):
    def wrapper():
        x = []
        y = []
        my = []

        x_fun, y_fun, params, mx, t_y_fun = function()

        for t in params:
            x.append(x_fun(t))
            y.append(y_fun(t))

        for x in mx:
            my.append(t_y_fun(x))
        

        graphs = [[x, y], [mx, my]]
        draw_multiple_graphs(graphs, 0.005, "red")
    return wrapper







def main():
    
    @pft_decorator
    def ex_4():
        params_ex_4 = [0, math.pi/4, math.pi/2, (3*math.pi) /4, math.pi, (math.pi*5)/4, (math.pi*3)/2, (math.pi*7)/4, math.pi*2]

        def fx_ex_4(i):
            return 2 * i - math.pi * math.sin(i)

    
        def fy_ex_4(i):
            return 2 - math.pi * math.cos(i)

        def fym_ex_4(x):
            m = -7.8546
            return m * x + 1.44

        mx = [ n for n in range(-2, 2) ]
        
        # x_fun, y_fun, params, mx, t_y_fun = function()
        return fx_ex_4,fy_ex_4, params_ex_4, mx, fym_ex_4
        


    ex_4()



if __name__ == "__main__":
    main()
