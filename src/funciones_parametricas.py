import math
from bokeh.plotting import figure, show

def funciones_parametricas(params, fx, fy, size):
    x = []
    y = []
    for i in params:
        y_n = fy(i)
        x_n = fx(i) 
        x.append(x_n)
        y.append(y_n)
        draw_graph(x, y, size, "red")
    print_table(x, y, params)


def draw_graph(x, y, size, color):
    plot = figure(plot_height=1000, plot_width=1000, title="Ecuaciones Parametricas", tools="save")
    plot.annulus(x=x, y=y, inner_radius=size,
              color=color, alpha=0.5)
    plot.line(x=x, y=y, line_width=3, line_alpha=0.6)
  
    show(plot)


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


if __name__ == "__main__":
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


    funciones_parametricas(params_ex_1, fx_ex_1, fy_ex_1, 0.05)
    print("\n"*4)
    funciones_parametricas(params_ex_2, fx_ex_2, fy_ex_2, 0.006)
