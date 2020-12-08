"""
    Functions for the Dates of linked list.

    Alejandro AS
    07-12-2020
"""

from models.Patient import Patient
from models.Dates import Date
from models.Doctor import Doctor
from database import DOCTORS, PATIENTS, DATES
from models.support_functions import select_gender, get_actual_uid

from lib.inputs import input_int, input_float, input_str_non_empty
from lib.util import clean_screen
from lib.menu import MenuOptions


from sorting.quick_sort import QuickSortPatientName, QuickSortDoctorName, QuickSortPatientAge, QuickSortDoctorAge
from database import save_changes


def validation():
    """
        Validates that it exist at least a single doctor and a single patient.
    """
    if PATIENTS.size() == 0 or DOCTORS.size() == 0:
        return False, "Patient or doctors missing\nCannot add with out users.\n SORRY!"

    return True, "All correct!"


def date_form(patient, doctor, actual_uid=None, actual_date_created=None):
    year = input_int("Date year:[2021-2024] ", False, 2024, 2021)
    month = input_int("Date month:[1-12] ", False, 12, 1)
    if month == 4:
        day = input_int("Date Day:[1-28] ", False, 28, 1, None)
    elif month in [4, 6, 9, 11]:
        day = input_int("Date Day: [1-30] ", False, 30, 1)
    else:
        day = input_int("Date Day: [1-31] ", False, 31, 1)

    date_date = f" {year} - {month} - {day} "

    hour = input_int("Date hour: [9 - 19]", False, 19, 9)
    min_hour = input_int("Date min: [00 - 59]", False, 59, 0)

    date_time = f" {hour}:{min_hour}"

    description = input_str_non_empty("Date description: ")

    if actual_uid == None and actual_date_created is None:
        date = Date(get_actual_uid(), doctor, patient,
                    date_date, date_time, description)
    else:
        date = Date(actual_uid, doctor, patient,
                    date_date, date_time, description)
        date.set_created(actual_date_created)
        date.update_modified()

    return date


def select_patient():
    idx = 0
    while True:
        clean_screen()
        print(PATIENTS.get(idx))
        s = input("[ s ] To select.")

        if s == "s":
            break

        if idx == PATIENTS.size() - 1:
            idx = 0
        else:
            idx += 1

    return PATIENTS.get(idx)


def select_doctor():
    idx = 0
    while True:
        clean_screen()
        print(DOCTORS.get(idx))
        s = input("[ s ] To select.")
        if s == "s":
            break

        if idx == DOCTORS.size() - 1:
            idx = 0
        else:
            idx += 1

    return DOCTORS.get(idx)


@save_changes
def add_date_end():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return False

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    DATES.append(date)
    input("Date added! All Correct")
    return True


def show_all_date():
    if DATES.size() == 0:
        print("Empty. No dates to show.")

    for i in range(DATES.size()):
        clean_screen()
        print(DATES.get(i))
        s = input("\n[ e ] To exit\n_")
        if s == 'e':
            break


@save_changes
def add_date_begin():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return False

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    DATES.preppend(date)
    print("Date added! All Correct")
    return True


@save_changes
def insert_date():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return

    if DATES.size() == 0:
        # if theres only a date
        add_date_end()
        input("There is no more items to insert in a specific position.")
        return True

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    idx = input_int("Index to insert: ", False, DATES.size() - 1, 0)
    DATES.insert(date, idx)
    print("Date added! All Correct")
    return True


@save_changes
def invert_date():
    if DATES.size() == 0:
        print("Empty. No dates to show.")

    DATES.reverse()
    print("The linked list of Dates has been reverse.")
    input("Check it in the [show all dates option]")
    return True


@save_changes
def delete_fist_date():
    if DATES.size() == 0:
        print("No dates to delete.")
        return False
    DATES.shift()
    input("SHIFT! the first Date was deleted.")
    return True


@save_changes
def delete_last_date():
    if DATES.size() == 0:
        print("No dates to delete.")
        return False
    DATES.pop()
    input("POP! The last Date was deleted.")
    return True


@save_changes
def remove_date():
    if DATES.size() == 0:
        print("Empty. No dates to remove.")
        return

    delete = False
    for i in range(DATES.size()):
        clean_screen()
        print(DATES.get(i))
        s = input("\n[ d ] To Delete\n[ e ] to exit\n_")
        if s == 'd':
            DATES.remove(i)
            input("Done! It was deleted.")
            delete = True
            break
        if s == 'e' or i == DATES.size() - 1:
            print("Okay i understand was a mistake")
            break
    return delete


@save_changes
def preinsert_date():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return

    if DATES.size() == 0:
        # if theres only a date
        add_date_end()
        input("There is no more items to insert in a specific position.")

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    idx = input_int("Index to insert: ", False, DATES.size() - 1, 0)
    DATES.preinstert(date, idx)
    input("Date added! All Correct")
    return True


@save_changes
def update_date():
    if DATES.size() == 0:
        print("Empty. No dates to delete.")
        return

    updated = False
    for i in range(DATES.size()):
        clean_screen()
        print(DATES.get(i))
        s = input("\n[ u ] To update\n[ e ] to exit\n_")
        if s == 'u':
            doctor = select_doctor()
            actual_date = DATES.get(i)
            new_date = date_form(actual_date.get_patient(
            ), doctor, actual_date.get_uid(), actual_date.get_created())
            DATES.update(new_date, i)
            input("Done! It was updated.")
            updated = True
            break
        if s == 'e' or i == PATIENTS.size() - 1:
            print("Okay i understand was a mistake")
            break
    return updated


def order_dates():
    if DATES.size() == 0:
        print("Empty, No dates to order.")
        return

    def print_specific_info(order, i):
        print(f"""
                    Name Doctor: {order.get(i).get_doctor().get_full_name()}
                    Doctor Age: {order.get(i).get_doctor().get_age()}
                    Name Patient: {order.get(i).get_patient().get_full_name()}
                    Patient Age: {order.get(i).get_patient().get_age()}
                    Date: {order.get(i).get_date()}  {order.get(i).get_time()}
                    Description: {order.get(i).get_description()}
                """)

    op = ["Order by doctor name.[STRING]", "Order by patient name [STRING].",
          "Oder by patient age. [NUMERIC]", "Order by doctor age. [NUMERIC]"]
    m = MenuOptions(op)
    selected = m.select()
    op_2 = ["Ascendent", "Descendent"]

    m_2 = MenuOptions(op_2)
    selected_2 = m_2.select()

    if selected == 0:
        print("Order by doctor Name.")
        quick_sort = QuickSortDoctorName(DATES)
        if selected_2 == 0:
            quick_sort.upward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)

        else:
            quick_sort.downward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)

    elif selected == 1:
        print("Order by patient Name.")
        quick_sort = QuickSortPatientName(DATES)
        if selected_2 == 0:
            quick_sort.upward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)
        else:
            quick_sort.downward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)

    elif selected == 2:
        print("Order by Patient Age.")
        quick_sort = QuickSortPatientAge(DATES)
        if selected_2 == 0:
            quick_sort.upward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)
        else:
            quick_sort.downward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)
    else:
        print("Order by Doctor Age.")
        quick_sort = QuickSortDoctorAge(DATES)
        if selected_2 == 0:
            quick_sort.upward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)
        else:
            quick_sort.downward()
            order = quick_sort.get_sorted()
            for i in range(order.size()):
                print_specific_info(order, i)
