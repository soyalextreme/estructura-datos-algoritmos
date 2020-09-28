"""
    27-09-2020
    Excersice 3 
    Estructura de Datos y algoritmos
    6to Semestre
    Article Reports
    Alejandro AS
"""


from first_partial_exercises.ex_2 import Report, print_format
from lib.menu.epp_menu import Menu
from lib.inputs import input_int, input_float


class Article():
    """
        Custom Article for this excersice.
    """
    # properties
    description = ""
    production_cost = 0

    def __init__(self, description, production_cost):
        self.production_cost = production_cost
        self.description = description

    def get_utility(self):
        return 1.20 * self.production_cost

    def get_taxes(self):
        return 0.15 * (self.production_cost + self.get_utility())

    def get_sell_price(self):
        return self.production_cost + self.get_utility() + self.get_taxes()


class Custom_Report(Report):
    """
        Custom Report that Inherits the prev excersice 
        report.
    """

    def __init__(self):
        """
            Init of the father class
        """
        Report.__init__(self)

    def show_report(self):
        """
            Overload this method of the father class.
        """
        total_cost = 0
        total_utility = 0
        total_taxes = 0
        total_price = 0

        print_format(["Article", "Production Cost",
                      "Utility", "Taxes", "Sell Price"])

        if len(self.articles) == 0:
            print("No hay articulos")
            return 0

        for article in self.articles:
            print_format(
                [article.description, article.production_cost, article.get_utility(), article.get_taxes(), article.get_sell_price()])
            total_cost += article.production_cost
            total_utility += article.get_utility()
            total_taxes += article.get_taxes()
            total_price += article.get_sell_price()

        print_format([f"Total {len(self.articles)}", total_cost,
                      total_utility, total_taxes, total_price])


def main():
    """
        Main function that handles the excersice 3.
    """
    r = Custom_Report()

    def handle_add():
        desc = input("Article Description: ")
        prod_cost = input_int("Production Cost: ", False)
        article = Article(desc, prod_cost)
        r.add_article(article)

    ARTICLE_REPORT_OPC = [
        (1, "ADD", handle_add),
        (2, "REPORT", r.show_report),
    ]

    m = Menu(ARTICLE_REPORT_OPC, exit_val=3)
    m.start()
