"""
    30-09-2020
    Excersice 9
    Estructura de Datos y algoritmos
    Average Trip
    6to Semestre
    Alejandro AS
"""

from lib.inputs import input_int, input_float
from lib.util import clean_screen
from lib.menu.epp_menu import Menu


class ReportTrip():
    trip_amount_persons = []
    trip_weight = []

    def __init__(self):
        pass

    def add_trip(self):
        print(f"Elevator Trip {len(self.trip_amount_persons) + 1}")
        amount = input_int(
            "Amount of people in the elevator trip: ", allow_negative=False)
        weight = round(input_float(
            "Weight in the elevator trip: ", allow_negative=False), 2)
        self.trip_amount_persons.append(amount)
        self.trip_weight.append(weight)
        print("Elevator Trip registered")

    def get_average_persons(self):
        return round(sum(self.trip_amount_persons) / len(self.trip_amount_persons), 2)

    def get_average_weight(self):
        return round(sum(self.trip_weight) / len(self.trip_weight), 2)

    def report(self):
        print("Day Stats")
        print("*"*30)
        print(f"""
                    Amount of trips: {len(self.trip_amount_persons)}
                    Amount of persons transported: {sum(self.trip_amount_persons)}
                    Weight Transported: {sum(self.trip_weight)} kg
                    Average of Persons per trip: {self.get_average_persons()}
                    Average of Weight per trip: {self.get_average_weight()} kg
        """)


def main():
    t = ReportTrip()
    OPC = [(1, "ADD TRIP", t.add_trip),
           (2, "SHOW STATS OF THE DAY", t.report)
           ]

    m = Menu(opcs=OPC, exit_val=3, still=False)
    m.start()
