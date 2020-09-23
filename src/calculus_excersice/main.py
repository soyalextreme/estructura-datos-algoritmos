import math
from lib.big_implements.parametric_function import pf_decorator



# x_fun y_fun params

def zone_a():
    
    @pf_decorator
    def ex_1():
        def x(t):
            return math.pow(t, 2) + t
        def y(t):
            return math.pow(t, 2) - t
        params = [ n for n in range(-2, 3) ]
        print("f(x) = t^2 + t\nf(y) = t^2 -t")
        return x, y, params

    
    @pf_decorator
    def ex_3():
        def x(t):
            return math.pow(math.cos(t), 2)
        def y(t):
            return 1 - math.sin(t)
        params =[0,]
        for n in range(1, 5):
            params.append(n/8 * math.pi )
        print("f(x) = cos^2(t)\nf(y) = 1 - sen(t)")
        return x, y, params



    ex_1()
    ex_3()
