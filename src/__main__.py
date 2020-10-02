from lib.menu.main_menu import main_menu
from lib.constants import PROYECT_STATE, EXCERCISE_STATE
# from calculus_excersice.main import zone_a as main
from sesions.s8_021020 import hola
from first_partial_exercises import main as main_ex
from calculus_excersice.main import zone_b

if __name__ == "__main__":
    if PROYECT_STATE:
        main_menu()
    elif EXCERCISE_STATE:
        main_ex()  # estructura de datos
        # zone_b()    # calculo vectorial
    else:
        hola()
