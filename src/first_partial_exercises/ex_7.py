"""
    29-09-2020
    Excersice 7
    Estructura de Datos y algoritmos
    STUDENTS FILTER
    6to Semestre
    Alejandro AS
"""


from lib.inputs import input_float, input_int, input_str_non_empty
from lib.prints import print_table_row
from lib.menu.epp_menu import Menu
from lib.util import clean_screen


OPTION_SEX = ('M', 'F', 'U')
OPTION_EYE_COLOR = ('Blue', 'Brown', 'Other')
OPTION_HAIR_COLOR = ('Brow', 'Blonde', 'Other')


def selection_opt(options, msg):
    selected = ''
    i = 0
    while selected != 's':
        clean_screen()
        print(msg)
        print(options[i])
        selected = input("[s] to select one option\n_ ")

        if selected == 's':
            continue

        if i == len(options) - 1:
            i = 0
        else:
            i += 1

    return options[i]


class Student():
    name = ''
    sex = ''
    age = 0
    height = 0
    weight = 0
    eye_color = ''
    hair_color = ''

    def __init__(self, name, sex, age, height, weight, eye_color, hair_color):
        self.name = name
        self.sex = sex
        self.age = age
        self.height = height
        self.weight = weight
        self.eye_color = eye_color
        self.hair_color = hair_color


class Group():

    students = []

    def __init__(self):
        self.students = []

    def add_student(self):
        student = self.student_form()
        self.students.append(student)
        print(f"{student.name} agregado correctamente")

    def student_form(self):
        name = input_str_non_empty("Student Name: ")
        age = input_int("Student age: ", allow_negative=False,
                        min_val=3, default=3)
        sex = selection_opt(OPTION_SEX, "Student gender: ")
        height = input_float("Student Height: ",
                             allow_negative=False, min_val=1, default=1)
        weight = input_float("Student Weight: ",
                             allow_negative=False, min_val=1, default=1)
        eye_color = selection_opt(OPTION_EYE_COLOR, "Student Eye color: ")
        hair_color = selection_opt(OPTION_HAIR_COLOR, "Student hair color: ")

        newStudent = Student(name, sex, age, height,
                             weight, eye_color, hair_color)
        return newStudent

    def show_report(self):

        if len(self.students) == 0:
            print("No students please add one.")
            return 0

        filter_boys = Group.filter_boys(self.students)
        Group.print_list(filter_boys)
        input("Enter to see the next List")
        filter_girls = Group.filter_girls(self.students)
        Group.print_list(filter_girls)

    @staticmethod
    def print_list(list_s):
        clean_screen()
        if(len(list_s) == 0):
            print("No results with the filter")
        for student in list_s:
            print(f'{student.name} | {student.sex} | {student.hair_color} | {student.eye_color} | {student.weight} kg. | {student.height} mts.')

    @staticmethod
    def filter_girls(l_student):
        print("Girls with blonde hair, Blue eyes and which height is between 1.65 1.70 and weight less than 55kg")
        print("*" * 20)
        filter_list = []
        for student in l_student:
            if student.sex == OPTION_SEX[1] and student.hair_color == OPTION_HAIR_COLOR[1] and student.eye_color == OPTION_EYE_COLOR[0] and student.weight < 55 and student.height >= 1.65 and student.height <= 1.75:
                filter_list.append(student)
        return filter_list

    @staticmethod
    def filter_boys(l_student):
        print("Boys with Brown Eyes which height is more than 1.70 and weight between 60 and 70 kgs")
        print("*" * 20)
        filter_list = []
        for student in l_student:
            if student.sex == OPTION_SEX[0] and student.eye_color == OPTION_EYE_COLOR[1] and student.height > 1.70 and student.weight <= 70 and student.weight >= 60:
                filter_list.append(student)
        return filter_list


def main():
    """
        Main function that handles this excersice.
    """

    group = Group()

    def handle_add():
        group.add_student()

    def handle_report():
        group.show_report()

    STUDENTS_EXC_OPC = [
        (1, "ADD STUDENT", handle_add),
        (2, "SHOW REPORT FILTERED", handle_report),
    ]

    m = Menu(STUDENTS_EXC_OPC, exit_val=3, still=False)
    m.start()
