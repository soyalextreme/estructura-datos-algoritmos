"""
    Main File to RUNNNNN!

    Check the settings for this
    Check the init_menu function
    Alejandro AS

    Enjoy my project!

"""

from settings import CLASSES_STATE, PROJECT_STATE
from menu.class_menu import init_menu
from menu.project_menu import main
from database import load, save

if __name__ == "__main__":
    if CLASSES_STATE == True:
        init_menu()
    if PROJECT_STATE == True:
        load()
        main()
        save()
