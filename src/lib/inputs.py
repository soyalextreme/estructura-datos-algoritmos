
def input_int(msg, allow_negative=True):
    """ Recibes input and handles error returning 0 by error default """
    try:
        if not allow_negative:
            return abs(int(input(msg)))
        return int(input(msg))
    except ValueError:
        return 0


def input_number_list(type="item", allow_negative_num=True, max_n=None, min_n=None):
    """ Creates a list and accepts dynamicly values form the user until ready, considerations only works with intgers """
    l = []
    s = ""
    def insert_item():
        item = input_int(f"Insert {type}: ") 
        
        # verifinyin negative num
        if not allow_negative_num:
            item = abs(item)
        
        # verifiyin the max and min value posible
        if max_n is not None and item > max_n:
            item = max_n
        elif min_n is not None and item < min_n:
            item = min_n

        

        l.append(item)
        s = input(f"Press [R] to stop\nEnter to add another {type}\n_").lower()
        return s

    while s != "r":
        s = insert_item()
    return l



    
    

