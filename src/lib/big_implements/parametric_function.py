import math
from lib.prints import print_table, draw_graph, draw_multiple_graphs


def pf_decorator(function):
    """ This decorator needs that the function returns three params. It
    generates two lists one for the x an one for the y using a parameter sucha
    as t in order to calculate

    Decorator Params=> 
                        x_fun => function that calculates position of x
                        y_fun => function that calculates position of y
                        paramas => parameter like time that dermines the
                        position

        Alejandro AS
    """
    def wrapper():
        x = []
        y = []
        
        # extracting the list and functions
        x_fun, y_fun, params = function()

        for t in params:
            x.append(x_fun(t))
            y.append(y_fun(t))
        print_table(x, y, params)
        draw_graph(x, y, 0.005, "red")
        return x, y
    return wrapper


def pft_decorator(function):
    """ This decorator need some functions and paramas for working. It
    generates and graphs the values of y and x depending on a parameter such as
    t. Also this function determines de slope of the function. Depending on m

        Params => 
                    x_fun => parametric function of x
                    y_fun => parametric function of y
                    params => a list of the t values that constrians
                    mx => list of the values given to x
                    t_y_fun => function that calculates y position of the point
                    in the slope.

        Alejandro AS
    """

    def wrapper():
        x = []
        y = []
        my = []

        x_fun, y_fun, params, mx, t_y_fun = function()

        for t in params:
            x.append(x_fun(t))
            y.append(y_fun(t))

        for l in mx:
            my.append(t_y_fun(l))
        


        print_table(x, y, params)
        graphs = [[x, y], [mx, my]]
        draw_multiple_graphs(graphs, 0.005, "red")

    return wrapper




def main():


    @pf_decorator
    def excercise():
        def x(t):
            return math.sin((1/2) * t)

        def y(t):
            return math.cos((1/2) * t)

        params = [-1*math.pi, -1*math.pi/2, 0, math.pi/2, math.pi]

        return x, y, params

    
    @pf_decorator
    def ex_2():
        def x(delta):
            return 1 * (delta - math.sin(delta))

        def y(delta):
            return 1 * (1 - math.cos(delta))

        params = [-1*math.pi, -1*math.pi/2, 0, math.pi/2, math.pi, 0.8414, -1,
                 math.pi /3]
        return x, y, params



    @pft_decorator
    def ex_3():
        def x(t):
            return math.pow(t, 2) - 4

        def y(t):
            return math.pow(t, 3) - (3 * t)

        def tangent_function(x):
            m = 1.33
            return m * x + 2

        params = [ n for n in range(-6, 6) ]
        params_tangent = [n for n in range(-20, 20)]


        return x, y, params, params_tangent, tangent_function


    @pft_decorator
    def ex_3_2():
        def x(t):
            return math.pow(t, 2) - 4

        def y(t):
            return math.pow(t, 3) - (3 * t)

        def tangent_function(x):
            m = -1.33
            return m * x - 2

        params = [ n for n in range(-6, 6) ]
        params_tangent = [n for n in range(-20, 20)]


        return x, y, params, params_tangent, tangent_function



    ex_3()
    ex_3_2()






#    excercise()
#    ex_2()




