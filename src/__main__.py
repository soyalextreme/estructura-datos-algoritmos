from lib.menu.main_menu import main_menu
from lib.constants import PROYECT_STATE
# from calculus_excersice.main import zone_a as main
from sesions.t5_240920 import main

if __name__ == "__main__":
    if PROYECT_STATE: 
        main_menu()
    else:
        main()


