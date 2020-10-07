from lib.menu.main_menu import main_menu
from lib.constants import PROJECT_STATE, EX_STATE
from first_partial_exercises import main as main_ex

if __name__ == "__main__":
    if PROJECT_STATE:
        main_menu()
    elif EX_STATE:
        main_ex()  # estructura de datos
    else:
        print("Test File")
