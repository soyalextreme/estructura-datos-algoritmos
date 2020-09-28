import math
from lib.big_implements.parametric_function import pf_decorator
import math


# x_fun y_fun params

def zone_a():

    @pf_decorator
    def ex_1():
        def x(t):
            return math.pow(t, 2) + t

        def y(t):
            return math.pow(t, 2) - t
        params = [n for n in range(-2, 3)]
        print("f(x) = t^2 + t\nf(y) = t^2 -t")
        return x, y, params

    @pf_decorator
    def ex_3():
        def x(t):
            return math.pow(math.cos(t), 2)

        def y(t):
            return 1 - math.sin(t)
        params = [0, ]
        for n in range(1, 5):
            params.append(n/8 * math.pi)
        print("f(x) = cos^2(t)\nf(y) = 1 - sen(t)")
        return x, y, params

    ex_1()
    ex_3()


def zone_b():

    @pf_decorator
    def ex_19():

        def x(t):
            return 3 + math.cos(t)

        def y(t):
            return 1 + 2 * math.sin(t)

        PI = math.pi

        paramas = [- PI / 2, -PI / 4, 0, PI / 4, PI / 2]

        return x, y, paramas

    @pf_decorator
    def ex_21():

        def x(t):
            return 5 * math.sin(t)

        def y(t):
            return 2 * math.cos(t)

        PI = math.pi

        params = [- PI, 0, PI, 2 * PI, 3 * PI, 4 * PI, 5 * PI]

        return x, y, params

    def separation():
        print("\n" * 3)
        print("*" * 30)

    # executing
    # ex_19()
    ex_21()
