"""
    27-09-2020
    Excersice 5
    Estructura de Datos y algoritmos
    6to Semestre
    Client Ticket Shop
    Alejandro AS
"""


from first_partial_exercises.ex_2 import Report
from lib.menu.epp_menu import Menu
from lib.inputs import input_int, input_float, input_str_non_empty
from lib.util import still_bool, clean_screen
from first_partial_exercises.ex_4 import Ticket, Article

clients = []


class Client():
    """
        Client but with the email for multiple ticket transactions.
    """
    name = ""
    email = ""

    def __init__(self, name, email):
        self.name = name
        self.email = email


def selection_client():
    """
        Function to select the client to add transaction
    """
    s = ""
    if len(clients) == 1:
        return clients[0]

    i = 0
    while s.lower() != "s":
        clean_screen()
        print(clients[i].name)
        s = input("[s] to select the user\n_")
        if s.lower() == "s":
            continue
        if i == len(clients) - 1:
            i = 0
        else:
            i += 1

    return clients[i]


def handle_add_ticket():
    """
        Function that handles to add a ticket.
    """
    if len(clients) == 0:
        print("No clients register for the moment, Cant do transactions.")
        print("Please, Add a client")
        return 0

    client = selection_client()

    t = Ticket(client.name)

    still = True

    while still:
        clean_screen()
        print(f"Client: {client.name}")
        print("Adding New Article")
        print("*" * 20)
        desc = input_str_non_empty("Description Article: ")
        amount = input_int("Amount: ", False, min_val=1, default=1)
        price = round(input_float("Price per product: ",
                                  False, min_val=1, default=1), 2)
        new_article = Article(desc, amount, price)
        t.add_article(new_article)

        still = still_bool("More Products? [y/n]: ")
    t.show_report()


def handle_add_client():
    """
        Function that handles to add a client
    """
    name = input_str_non_empty("Client Name: ")
    email = input_str_non_empty("Client email: ")
    c = Client(name, email)
    clients.append(c)
    print(f"{name} Added to clients")


def main():
    """
        Main function that handles this excersice.
    """

    ARTICLE_REPORT_OPC = [
        (1, "ADD CLIENT", handle_add_client),
        (2, "NEW TRANSACTION", handle_add_ticket),
    ]

    m = Menu(ARTICLE_REPORT_OPC, exit_val=3, still=False)
    m.start()
