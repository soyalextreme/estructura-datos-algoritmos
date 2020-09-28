"""
    26-09-2020
    Excersice 2 
    Estructura de Datos y algoritmos
    6to Semestre
    Article Reports
    Alejandro AS
"""

from lib.menu.epp_menu import Menu
from lib.inputs import input_int, input_float, input_str_non_empty


def print_format(l):
    chain = ""
    for i in l:
        chain += "|  {0:^25}  |".format(i)
    print(chain)
    print("*" * (len(l) * 35))


class Article():
    """
        Article Class for the report of the products produced
        description => string
        amount_produced => integer
        extra_materia_cost => Float
        base_cost => Integer 
    """
    description = ""
    amount_produced = 0
    extra_material_cost = 0
    base_cost = 0

    def __init__(self, description, amount_produced, extra_material_cost, base_cost):
        """
            Constructor
            Description => String
            amount_produced => integer
            extra_material_cost => float
            base_cost => integer
        """
        self.description = description
        self.amount_produced = amount_produced
        self.extra_material_cost = extra_material_cost
        self.base_cost = base_cost

    def production_cost(self):
        """
            Calculation of the production cost.
        """
        return (self.amount_produced * self.extra_material_cost) + self.base_cost


class Report():
    """
        Report Class for the multiple articles collection.
        Attributes:
        articles => Collection of articles
        total => Final cost of all the articles cost => Integer
    """
    articles = []
    total = 0

    def __init__(self):
        self.articles = []

    def add_article(self, article):
        """ 
            Function that appeds the a article to the collection
        """
        self.articles.append(article)

    def show_report(self):
        """
            Show the report 
            showing  all the products 
            showing the total cost of production of all the productos
        """
        self.total = 0
        print_format(["Article", "Amount Produced", "Factor cost",
                      "Base Cost", "Production Cost"])
        if len(self.articles) == 0:
            print("No articles added, Please Add at least one")
            return 0

        for article in self.articles:
            print_format([article.description, article.amount_produced,
                          article.extra_material_cost, article.base_cost, article.production_cost()])
            self.total += article.production_cost()

        print_format([
            f"Total Articles {len(self.articles)}", "", "", "", self.total])


def main():
    """
        Main function that handles the excersice 2.
    """
    r = Report()

    def handle_add():
        desc = input_str_non_empty("Article Description: ")
        amount = input_int("Article Amount: ", False, min_val=1, default=1)
        ex_factor = input_float("Article Factor Cost: ", False)
        base_cost = input_int("Article base cost: ",
                              False, min_val=1, default=1)

        article = Article(desc, amount, ex_factor, base_cost)
        r.add_article(article)

    ARTICLE_REPORT_OPC = [
        (1, "ADD", handle_add),
        (2, "REPORT", r.show_report),
    ]

    m = Menu(ARTICLE_REPORT_OPC, exit_val=3)
    m.start()
