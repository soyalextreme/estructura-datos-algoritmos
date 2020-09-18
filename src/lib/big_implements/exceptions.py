"""
    Homework | Exceptions
    18-09-2020
    Alejandro AS
"""

# how to create a custom exception
class CustomError(Exception):
    # class need to extends from BaseException
    # you can declare a constructor to recibe some custom values like a message
    def __init__(self, *args):
        """ This method inits the Error can or not recibe a list of args """
        if args:
            self.message = args[0]
        else:
            self.message = None

   # str method is the one that returns the str that show when rised when rise. 
    def __str__(self):
        """ Method that returns the error string  """
        return "CustomError | This is a custom error class"


def run_custom_exception():
    """ Function that helps you try the custom errors """
    raise CustomError


def run_manage_custom_exception():
    """ Function that helps you try the manage of custom error """
    try:
        raise CustomError
    except CustomError as e:
        print(f"managing the custom error {e}")




