
from lib.inputs import input_str_non_empty, input_float
from lib.prints import print_table_row
from lib.menu.epp_menu import Menu


AMOUNT_PARTIALS = 3


class Student():

    def __init__(self, name, calif):
        self.name = name
        self.calif = calif

    def get_average(self):
        prom = round(sum(self.calif) / AMOUNT_PARTIALS, 2)
        if prom < 7:
            return "NA"
        return prom


class Group():

    def __init__(self):
        self.students = []

    def add_student(self):
        name = input_str_non_empty("Student name: ")
        califs = []
        for i in range(AMOUNT_PARTIALS):
            n = round(input_float(
                f"Calification {i + 1} Partial: ", allow_negative=False, max_val=10), 2)
            califs.append(n)
        s = Student(name, califs)
        self.students.append(s)
        print(f"{name} fue agregado corectamente")

    def show_report(self):
        if len(self.students) == 0:
            print("No students to make report")
            return

        print("""
                Calification Report
        """)
        print_table_row(["Name", "Calif"])
        for student in self.students:
            print_table_row([student.name, student.get_average()])
        print_table_row([f"Total Students {len(self.students)}", ""])


def main():
    group = Group()

    CALIF_REPORT = [
        (1, "ADD STUDENT", group.add_student),
        (2, "SHOW CALIF REPORT", group.show_report),
    ]

    m = Menu(CALIF_REPORT, exit_val=3, still=False)
    m.start()
