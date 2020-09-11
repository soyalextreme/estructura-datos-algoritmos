import math
from lib.inputs import input_int
from lib.prints import print_table
from bokeh.plotting import figure, show

def funciones_cicloides(radius, teta_angle):
    x = []
    y = []

    for t in teta_angle:
        x_ = radius * (t - math.sin(t))
        y_  = radius * (1 - math.cos(t))
        x.append(x_)
        y.append(y_)
    
    draw_graph(x,y,0.5,"red")
    print_table(x, y, teta_angle)


def draw_graph(x, y, size, color):
    plot = figure(plot_height=1000, plot_width=1000, title="Ecuaciones Parametricas", tools="save")
    plot.annulus(x=x, y=y, inner_radius=size,
              color=color, alpha=0.5)
    plot.line(x=x, y=y, line_width=3, line_alpha=0.6)
  
    show(plot)


def main():
    r = input_int("Circle Radius:\n") 
    n_p = input_int("Until which PI value you wanna graph:\n")
    n_t = input_int("How many PI values for generating teta angles:\n")
    val = 0
    teta_angle = []
    for n in range(n_t):
        while val < n_p * math.pi:
            val += 1/ n_t * math.pi 
            teta_angle.append(val)


    funciones_cicloides(r, teta_angle=teta_angle)

if __name__ == "__main__":
    main()
