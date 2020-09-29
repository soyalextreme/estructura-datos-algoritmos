"""
    28-09-2020
    Excersice 6
    Estructura de Datos y algoritmos
    Acount bank
    6to Semestre
    Alejandro AS
"""
from lib.inputs import input_str_non_empty, input_float
from lib.util import clean_screen
from lib.prints import print_table_row


class AcountStatus():
    owner_name = ""
    initial_salary = 0
    salary = ""
    movements = []

    def __init__(self, owner_name, salary):
        self.owner_name = owner_name
        self.salary = salary
        self.initial_salary = salary

    def selection_movement(self):
        print("NEW MOVEMENT")
        options = ["Deposit", "Retirement"]
        s = ''
        i = 0
        while s != 's':
            clean_screen()
            print(options[i].upper())
            s = input("[s] To select\n_").lower()
            if s == 's':
                continue

            if i == len(options) - 1:
                i = 0
            else:
                i += 1
        return options[i]

    def show_transactions_report(self):
        clean_screen()
        print(f"""
                                                Acount Status
              Name: {self.owner_name}                
              Initial Salary: {self.initial_salary}
        """)
        print_table_row(["Movement", "Deposit", "Retirement", "Salary"])
        total_deposit = 0
        total_retiremts = 0
        for i in range(len(self.movements)):
            if self.movements[i][0] > 0:
                print_table_row([1, self.movements[i][0],
                                 "", self.movements[i][1]])
                total_deposit += self.movements[i][0]
            else:
                print_table_row(
                    [i + 1, "", abs(self.movements[i][0]), self.movements[i][1]])
                total_retiremts += abs(self.movements[i][0])
        print_table_row(["Totales", total_deposit,
                         total_retiremts, self.salary])

    def new_movement(self):
        ready = ''
        while ready != 'r':
            clean_screen()
            option = self.selection_movement()

            clean_screen()
            print(option.upper())
            amount = input_float(
                f"Give me the amount to {option}: ", min_val=20, default=20)
            round(amount, 3)
            if option.lower() == 'deposit':
                self.salary += amount
                self.movements.append((amount, self.salary))
                print(f"Deposit of {amount}")
            else:
                if self.salary - amount > 0:
                    self.salary -= amount
                    self.movements.append((-1 * amount, self.salary))
                    print(f"Retirement of {amount}")
                else:
                    print("Ups! Invalid Transaciton not enough money")
            input("_")

            clean_screen()
            print(f"Salary: {self.salary}")
            ready = input(
                "[r] To exit and print the report\n[Enter] For new Transaction\n_")

        self.show_transactions_report()


def main():
    owner_name = input_str_non_empty("Name of the owner of the acount: ")
    init_salary = input_float("Initial Salary: ", False, min_val=1, default=1)
    a = AcountStatus(owner_name, init_salary)
    a.new_movement()
