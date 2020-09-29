from first_partial_exercises import ex_1, ex_2, ex_3, ex_4, ex_5, ex_6, ex_7


def learning_tables():
    print("Learning tables")


def article_cost():
    print("Article cost")


MAIN_MENU = [(1, "Learning Tables", ex_1.main),
             (2, "Article Report and Cost", ex_2.main),
             (3, "Article Taxes Utility Report", ex_3.main),
             (4, "Shop Ticket Report", ex_4.main),
             (5, "Shop Ticket Report plus Clients", ex_5.main),
             (6, "Casher Withdrawal", ex_6.main),
             (7, "Student List Filter", ex_7.main)
             ]
