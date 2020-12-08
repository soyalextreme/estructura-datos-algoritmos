"""
    Function for the linked list operations with the doctor.

    - CRUD functions

    Alejandro AS
    06-12-2020
"""


from models.Doctor import Doctor, create_doctor, update_doctor as update_doctor_form
from database import DOCTORS, DATES
from lib.inputs import input_str_non_empty, input_int, input_float
from lib.util import clean_screen
from models.support_functions import select_gender, get_actual_uid

from database import save_changes


@save_changes
def add_doctor():
    """
        Add a doctor to a linked list.
    """
    d = create_doctor()
    DOCTORS.append(d)
    clean_screen()
    input(f"Congrats!!! Doctor {d.get_name()} Added Successfully")
    return True


def show_all_doctor():
    """
        Shows all doctors from the actual linked list.
    """
    if DOCTORS.size() == 0:
        print("No Doctors to show")
        return

    for i in range(DOCTORS.size()):
        clean_screen()
        print(DOCTORS.get(i))
        s = input("\n[ e ] To exit\n_")
        if s == 'e':
            break


# def search_dates_doctor_id(i):
#     """
#         Deletes doctor dates in the list when deleting a doctor.
#     """
#     uid = DOCTORS.get(i).get_uid()
#     founded = False
#     for j in range(DATES.size()):
#         date = DATES.get(j)
#         if date.get_doctor().get_uid() == uid:
#             founded = True
#     if founded:
#         print("This person has dates. Please delete those.")
#         return False


@save_changes
def delete_doctor():
    """
        Delete a doctor from the linked list with the function remove.
    """
    if DOCTORS.size() == 0:
        print("No Doctors to delete.")
        return

    deleted = None
    for i in range(DOCTORS.size()):
        clean_screen()
        print(DOCTORS.get(i))
        s = input("\n[ d ] To Delete\n[ e ] to exit\n_")
        if s == 'd':
            # search_dates_doctor_id(i)
            DOCTORS.remove(i)
            input("Done! It was deleted.")
            deleted = True
            break
        if s == 'e' or i == DOCTORS.size() - 1:
            print("Okay i understand was a mistake")
            break
    return deleted


def update_dates_from_doctor(i, doctor):
    """
        Updates the dates of the doctor that was updated.
    """
    uid = DOCTORS.get(i).get_uid()
    updated = False
    for j in range(DATES.size()):
        date = DATES.get(j)
        if date.get_doctor().get_uid() == uid:
            date.set_doctor(doctor)
            updated = True
    if updated:
        print("Dates of this doctor were modified.")


@save_changes
def update_doctor():
    """
        Updates a doctor from the linked list with the function update.
    """
    if DOCTORS.size() == 0:
        print("No doctors to update.")
        return

    updated = None
    for i in range(DOCTORS.size()):
        clean_screen()
        print(DOCTORS.get(i))
        s = input("\n[ u ] To update\n[ e ] to exit\n_")
        if s == 'u':
            d = update_doctor_form(i)
            DOCTORS.update(d, i)
            update_dates_from_doctor(i, d)
            input("Done! It was updated.")
            updated = True
            break
        if s == 'e' or i == DOCTORS.size() - 1:
            print("Okay i understand was a mistake")
            break
    return updated
