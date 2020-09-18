from lib.menu.main_menu import main_menu
from lib.constants import PROYECT_STATE
from sesions.s4_150920 import main

if __name__ == "__main__":
    if PROYECT_STATE: 
        main_menu()
    else:
        main()


