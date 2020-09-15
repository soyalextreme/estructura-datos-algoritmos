import math
from lib.inputs import input_int
from lib.prints import print_table, draw_graph


def cycloid_function(radius, teta_angle):
    """ This function calculates and graphs the cycloid function depending on the paramas
        params:
            radius of the circle
            teta angle => the limit of the cycloid
    """
    x = []
    y = []

    for t in teta_angle:
        x_ = radius * (t - math.sin(t))
        y_  = radius * (1 - math.cos(t))
        x.append(x_)
        y.append(y_)
    
    draw_graph(x,y,0.5,"red")
    print_table(x, y, teta_angle)


def main():
    print("CYCLODE FUNCTION - OPTION 7")
    print("*"*20)
    print("Advice: Not allowing negative numbers")
    r = input_int("Circle Radius:\n", allow_negative=False) 
    n_p = input_int("Until which PI value you wanna graph:\n", allow_negative=False)
    n_t = input_int("How many PI values for generating teta angles:\n", allow_negative=False)
    val = 0
    teta_angle = []
    for n in range(n_t):
        while val < n_p * math.pi:
            val += 1/ n_t * math.pi 
            teta_angle.append(val)
    cycloid_function(r, teta_angle=teta_angle)

if __name__ == "__main__":
    main()
