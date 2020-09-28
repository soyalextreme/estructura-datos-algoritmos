"""
    27-09-2020
    Excersice 4
    Estructura de Datos y algoritmos
    6to Semestre
    Article Reports
    Alejandro AS
"""


from first_partial_exercises.ex_2 import Report, print_format
from lib.menu.epp_menu import Menu
from lib.inputs import input_int, input_float, input_str_non_empty
from lib.util import still_bool, clean_screen


class Article():
    description = ""
    amount = 0
    unitary_price = 0

    def __init__(self, description, amount, unitary_price):
        self.description = description
        self.amount = amount
        self.unitary_price = unitary_price

    def get_total(self):
        return self.unitary_price * self.amount


class Ticket(Report):
    client_name = ""

    def __init__(self, client_name):
        Report.__init__(self)
        self.client_name = client_name

    def show_report(self):
        clean_screen()
        subtotal = 0
        taxes = 0
        total = 0

        print("TICKET")
        print(f"Client Name: {self.client_name}")
        print_format(["Article", "Amount", "Unitary Price", "Total"])
        for article in self.articles:
            print_format([article.description, article.amount,
                          article.unitary_price, article.get_total()])
            subtotal += article.get_total()
        taxes = 0.15 * subtotal
        total = subtotal + taxes
        print_format(["", "", "Subtotal:", subtotal])
        print_format(["", "", "Taxes 15%:", taxes])
        print_format(["", "",  "Total:", total])


def main():
    """
        Main function that handles the excersice 4.
    """
    client_name = input("Client Name: ")

    t = Ticket(client_name)
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
