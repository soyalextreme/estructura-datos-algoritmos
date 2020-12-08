"""
    Scripts for the tree structure of the doctor
    TAKES a random ID as a number to order the structure.
    Unique key for this nodes.

    Alejandro AS
    06-12-2020
"""


import random

from lib.menu import Menu, MenuOptions
from lib.inputs import input_str_non_empty, input_int, input_float
from lib.util import clean_screen
from models.support_functions import select_gender, get_actual_uid

from database import DOCTORS, PATIENTS, DOCTORS_TREE, DATES

from models.Doctor import Doctor, create_doctor, update_doctor as update_doctor_form


def add_doctor_tree():
    """
        Adding a doctor to the tree
    """
    name = input_str_non_empty("Doctor Name: ")
    last_name = input_str_non_empty("Doctor LastName: ")
    email = input_str_non_empty("Doctor Email: ")
    gender = select_gender()
    age = input_int("Doctor Age: ", False, 75, 18)
    medical_specialty = input_str_non_empty("Doctor Specialty: ")
    d = Doctor(name, last_name, email,
               random.randint(0, 99999999), gender, age, medical_specialty)
    DOCTORS_TREE.insert([d.get_uid(), d])
    clean_screen()
    print("Congrats!!! Doctor Added Successfully")


def show_doctors_tree():
    """
        Shows all doctors depending on the tree order selected.
    """

    opcs = ["Postorder", "Innorder", "Preorder"]
    m = MenuOptions(opcs)
    op = m.select()

    if op == 0:
        l = DOCTORS_TREE.postorder()
    elif op == 1:
        l = DOCTORS_TREE.innorder()
    else:
        l = DOCTORS_TREE.preorder()

    try:
        for i in l:
            print(f"""
                {i[0]} {i[1]}
            """)
    except:
        print("NO ELEMENTS\nAdd a doctor first!\n" + "=" * 30)


def delete_doctor_tree():
    """
        Finds and delete a doctor by ID.
    """
    uid = input_int("Id to delete: ", False)
    feedBack = DOCTORS_TREE.delete(uid)
    print(feedBack)


def find_doctor_tree():
    """
        Finds a doctor by ID and i show that to you.
    """
    uid = input_int("Id to find: ", False)
    doctor = DOCTORS_TREE.find(uid)
    print(doctor)
