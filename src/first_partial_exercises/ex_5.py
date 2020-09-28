"""
    27-09-2020
    Excersice 5
    Estructura de Datos y algoritmos
    6to Semestre
    Article Reports
    Alejandro AS
"""


from first_partial_exercises.ex_2 import Report, print_format
from lib.menu.epp_menu import Menu
from lib.inputs import input_int, input_float, input_str_non_empty
from lib.util import still_bool, clean_screen


from first_partial_exercises.ex_4 import Ticket, Article

CLIENTS = []


class Client():
    name = ""
    email = ""

    def __init__(self, name, email):
        self.name = name
        self.email = email


def selection_client():
    s = ""
    if len(CLIENTS) == 1:
        return CLIENTS[0]

    i = 0
#    increment = 1
    while s.lower() != "s":
        clean_screen()
        print(CLIENTS[i].name)
        s = input("[s] to select the user")
        if s.lower() == "s":
            continue
        if i == len(CLIENTS) - 1:
            i = 0
        else:
            i += 1

    return CLIENTS[i]


def handle_add_ticket():
    if len(CLIENTS) == 0:
        print("No clients register for the momento, Cant do transactions.")
        print("Please, Add a client")
        return 0

    client = selection_client()

    t = Ticket(client.name)

    still = True

    while still:
        print("Adding New Article")
        print("*" * 20)
        desc = input_str_non_empty("Description Article: ")
        amount = input_int("Amount: ", False, min_val=1, default=1)
        price = input_int("Price per product: ", False, min_val=1, default=1)
        new_article = Article(desc, amount, price)
        t.add_article(new_article)

        still = still_bool("More Products? [y/n]: ")
    t.show_report()


def handle_add_client():
    name = input_str_non_empty("Client Name: ")
    email = input_str_non_empty("Client email: ")
    c = Client(name, email)
    CLIENTS.append(c)
    input(f"{name} Added to clients")
    clean_screen()


def main():

    ARTICLE_REPORT_OPC = [
        (1, "ADD CLIENT", handle_add_client),
        (2, "NEW TRANSACTION", handle_add_ticket),
    ]

    m = Menu(ARTICLE_REPORT_OPC, exit_val=3)
    m.start()
