
def input_int(msg):
    """ Recibes input and handles error returning 0 by error default """
    try:
        return int(input(msg))
    except ValueError:
        return 0


def input_number_list(type="item"):
    l = []
    s = ""
    def insert_item():
        item = input_int(f"Insert {type}: ") 
        l.append(item)
        s = input(f"Press [R] to stop\nEnter to add another {type}").lower()
        return s

    while s != "r":
        s = insert_item()
    return l


def print_title(title):
    """ Prints the tile with separation an in uppercase """
    print(title.upper())
    print("*" * 25)   

