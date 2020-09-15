""" Functions related to print somthing to the user by the system """
import os
from bokeh.plotting import figure, show


def print_table(x, y, parameter):
    """
        This function prints a table and gives a format to it. This functions
        is base to print f(x) functions so recibes de following parameters.
        params: x type list
                y type list
                parameter type list
    """
    op = 0
    while op < len(parameter):
        print("*"*104)
        if op == 0:
            print("* {0:^30}  |  {1:^30}  |  {2:^30} *".format("Parameter", "x",  "y"))
            print("*"*104)
        print("* {0:^30}  |  {1:^30}  |  {2:^30} *".format(parameter[op], x[op],  y[op]))
        print("*"*104)
        op += 1


def print_title(title):
    """ Prints the tile with separation by ****** an in uppercase """
    print(title.upper())
    print("*" * 25)   


def draw_graph(x, y, size, color):
    """ This function graph the dots and the line of a function
        params: x => list
                y => list 
                size 
                color
    """
    plot = figure(plot_height=1000, plot_width=1000, title="Ecuaciones Parametricas", tools="save")
    plot.annulus(x=x, y=y, inner_radius=size,
              color=color, alpha=0.5)
    plot.line(x=x, y=y, line_width=3, line_alpha=0.6)
    show(plot)

