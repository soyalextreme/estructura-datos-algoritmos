from lib.menu.main_menu import main_menu
from lib.constants import PROYECT_STATE, EXCERCISE_STATE
# from calculus_excersice.main import zone_a as main
from sesions.t5_240920 import main
from first_partial_exercises import main as main_ex

if __name__ == "__main__":
    if PROYECT_STATE:
        main_menu()
    elif EXCERCISE_STATE:
        main_ex()
    else:
        main()
