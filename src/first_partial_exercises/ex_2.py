

from lib.menu.epp_menu import Menu
from lib.inputs import input_int, input_float


def print_format(a, b, c, d, e):
    print("|  {0:^25}  |  {1:^25}  |  {2:^25}  | {3:^25}  |  {4:^25}  |".format(a, b, c, d, e))
    print("*"*150)



class Article():
    description = ""
    amount_produced = 0
    extra_material_cost = 0
    base_cost = 0
    

    def __init__(self, description, amount_produced, extra_material_cost, base_cost):
        self.description = description
        self.amount_produced = amount_produced 
        self.extra_material_cost = extra_material_cost
        self.base_cost = base_cost

    
    def production_cost(self):
        return (self.amount_produced * self.extra_material_cost) + self.base_cost





class Report():
    articles = []
    total = 0

    def add_article(self, article):
        self.articles.append(article)


    def show_report(self):

        print_format("Article", "Amount Produced", "Factor cost", "Base Cost", "Production Cost")
        if len(self.articles) == 0:
            print("No articles :C")


        for article in self.articles:
            print_format(article.description, article.amount_produced,
             article.extra_material_cost, article.base_cost, article.production_cost())
            self.total += article.production_cost()
        
        print_format(f"Total Articles {len(self.articles)}", "" , "", "", self.total)

        


def main():
    r = Report()


    def handle_add():
        desc = input("Article Description: ")
        amount = input_int("Article Amount: ", False)
        ex_factor = input_float("Article Factor Cost: ", False)
        base_cost = input_int("Article base cost: ", False)


        article = Article(desc, amount, ex_factor, base_cost)
        r.add_article(article)

    ARTICLE_REPORT_OPC = [
        (1, "ADD", handle_add),
        (2, "REPORT", r.show_report),
    ]


    m = Menu(ARTICLE_REPORT_OPC, exit_val=3)
    m.start()




            

            


    