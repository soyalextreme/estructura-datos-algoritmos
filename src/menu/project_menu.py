import random

from lib.menu import Menu, MenuOptions
from lib.inputs import input_str_non_empty, input_int, input_float
from lib.util import clean_screen
from models.support_functions import select_gender, get_actual_uid

from database import DOCTORS, PATIENTS, DOCTORS_TREE, DATES

from models.Doctor import Doctor, create_doctor, update_doctor as update_doctor_form
from models.Patient import Patient
from models.Dates import Date

from sorting.quick_sort import QuickSortDoctorName, QuickSortPatientName, QuickSortPatientAge, QuickSortDoctorAge

from scripts.doctor_tree import add_doctor_tree, delete_doctor_tree, find_doctor_tree, show_doctors_tree
from scripts.doctor_linked import add_doctor, show_all_doctor, delete_doctor, update_doctor
from scripts.patient_linked import add_patient, show_all_patient, delete_patient, update_patient
from scripts.dates_linked import add_date_end, add_date_begin, insert_date, preinsert_date, delete_fist_date, delete_last_date, remove_date, show_all_date, invert_date, update_date, order_dates


DATES_OPTIONS = [(1, "Add a Date to the end. [APPEND]", add_date_end),
                 (2, "Add a Date to the begining. [PREPPEND]", add_date_begin),
                 (3, "Insert a Date to a position. [INSERT]", insert_date),
                 (4,
                  "Insert a Date to a position before. [PREINSERT]", preinsert_date),
                 (5, "Delete the first Date [SHIFT]", delete_fist_date),
                 (6, "Delete the last Date [POP]", delete_last_date),
                 (7, "Remove a Date in a postition. [REMOVE]", remove_date),
                 (8, "Show all the dates. [SHOW]", show_all_date),
                 (9, "Invert the list of dates [INVERT]", invert_date),
                 (10, "Update date Information [UPDATE]", update_date),
                 (11, "Order the list. [ORDER]", order_dates)
                 ]


DOCTOR_OPS = [(1, "Add a Doctor.", add_doctor),
              (2, "Remove a Doctor.", delete_doctor),
              (3, "Update a Doctor.", update_doctor),
              (4, "Show all doctors.", show_all_doctor),
              ]

PATIENT_OPS = [(1, "Add a Patient", add_patient),
               (2, "Remove a Patient", delete_patient),
               (3, "Update a Patient", update_patient),
               (4, "Show all Patients", show_all_patient)
               ]

TREES_OPS = [(1, "Add a Doctor", add_doctor_tree),
             (2, "Delete a Doctor", delete_doctor_tree),
             (3, "Find a doctor", find_doctor_tree),
             (4, "Show Doctors tree", show_doctors_tree)
             ]


def doctors():
    m = Menu(DOCTOR_OPS, 5, False)
    m.start()


def patient():
    m = Menu(PATIENT_OPS, 5, False)
    m.start()


def dates():
    m = Menu(DATES_OPTIONS, 12, False)
    m.start()


def trees():
    m = Menu(TREES_OPS, 5)
    m.start()


MAIN_OPC = [(1, "Doctor Menu", doctors),
            (2, "Patients Menu", patient),
            (3, "Dates Menu", dates),
            (4, "Test trees in search", trees)
            ]


def main():
    title = """
.---.                              .-.        .---.  _              .-.  
: .; :                            .' `.       : .--':_;             : :  
:  _.'.--.  .--. .-..-. .--.  .--.`. .'.--.   : `;  .-.,-.,-. .--.  : :  
: :   : ..'' .; :: :; :' '_.''  ..': :' .; :  : :   : :: ,. :' .; ; : :_ 
:_;   :_;  `.__.'`._. ;`.__.'`.__.':_;`.__.'  :_;   :_;:_;:_;`.__,_;`.__;
                  .-. :                                                  
                  `._.'                                                  
     """
    m = Menu(MAIN_OPC, 5, True, True,
             f"{title} \n Alejandro Andrade\n My dates.\n\nEnter to start")
    m.start()
