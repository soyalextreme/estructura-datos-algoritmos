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

        for x in mx:
            my.append(t_y_fun(x))
        

        graphs = [[x, y], [mx, my]]
        draw_multiple_graphs(graphs, 0.005, "red")

    return wrapper






