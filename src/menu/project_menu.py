import random

from lib.menu import Menu, MenuOptions
from lib.inputs import input_str_non_empty, input_int, input_float
from lib.util import clean_screen
from models.support_functions import select_gender, get_actual_uid

from database import DOCTORS, PATIENTS, DOCTORS_TREE, DATES

from models.Doctor import Doctor, create_doctor, update_doctor as update_doctor_form
from models.Patient import Patient
from models.Dates import Date

# MENU FUNCTIONS

# TREE FUNCTIONS


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
    uid = input_int("Id to delete: ", False)
    feedBack = DOCTORS_TREE.delete(uid)
    print(feedBack)


def find_doctor_tree():
    uid = input_int("Id to delete: ", False)
    doctor = DOCTORS_TREE.find(uid)
    print(doctor)


# DOCTORS MENU
def add_doctor():
    """
        Add a doctor to a linked list.
    """
    d = create_doctor()
    DOCTORS.append(d)
    clean_screen()
    print(f"Congrats!!! Doctor {d.get_name()} Added Successfully")


def show_all_doctor():
    for i in range(DOCTORS.size()):
        clean_screen()
        print(DOCTORS.get(i))
        s = input("\n[ e ] To exit\n_")
        if s == 'e':
            break


def delete_doctor():
    for i in range(DOCTORS.size()):
        clean_screen()
        print(DOCTORS.get(i))
        s = input("\n[ d ] To Delete\n[ e ] to exit\n_")
        if s == 'd':
            DOCTORS.remove(i)
            print("Done! It was deleted.")
            break
        if s == 'e' or i == DOCTORS.size() - 1:
            print("Okay i understand was a mistake")
            break


def update_doctor():
    for i in range(DOCTORS.size()):
        clean_screen()
        print(DOCTORS.get(i))
        s = input("\n[ u ] To update\n[ e ] to exit\n_")
        if s == 'u':
            d = update_doctor_form(i)
            DOCTORS.update(d, i)
            print("Done! It was updated.")
            break
        if s == 'e' or i == DOCTORS.size() - 1:
            print("Okay i understand was a mistake")
            break

# patient MENU


def add_patient():
    name = input_str_non_empty("Patient Name: ")
    last_name = input_str_non_empty("Patient Last Name: ")
    email = input_str_non_empty("Patient Email: ")
    gender = select_gender()
    age = input_int("Patient Age: ", False, 75, 1)
    height = input_float("Patient Height:[mts] ", False, 2.45, 0.5)
    weight = input_float("Patient Weight:[kgs] ", False, 200, 1)
    symptoms = input_str_non_empty("Patient Symptoms: ")
    p = Patient(name, last_name, email, get_actual_uid(),
                gender, age, height, weight, symptoms)
    PATIENTS.append(p)
    clean_screen()
    print(f"Congrats!!! Patient {name} Added Successfully")


def show_all_patient():
    for i in range(PATIENTS.size()):
        clean_screen()
        print(PATIENTS.get(i))
        s = input("\n[ e ] To exit\n_")
        if s == 'e':
            break


def delete_patient():
    for i in range(PATIENTS.size()):
        clean_screen()
        print(PATIENTS.get(i))
        s = input("\n[ d ] To Delete\n[ e ] to exit\n_")
        if s == 'd':
            PATIENTS.remove(i)
            print("Done! It was deleted.")
            break
        if s == 'e' or i == PATIENTS.size() - 1:
            print("Okay i understand was a mistake")
            break


def update_patient_form(idx):
    actual_patient = PATIENTS.get(idx)
    name = input_str_non_empty(
        f"Patient Name: [{actual_patient.get_name()}]  ")
    last_name = input_str_non_empty(
        f"Patient Last Name: [{actual_patient.get_last_name()}]  ")
    email = input_str_non_empty(
        f"Patient Email: [{actual_patient.get_email()}]  ")
    gender = select_gender()
    age = input_int(
        f"Patient Age: [{actual_patient.get_age()}]  ", False, 75, 1)
    height = input_float(
        f"Patient Height:[mts] [{actual_patient.get_height()}]  ", False, 2.45, 0.5)
    weight = input_float(
        f"Patient Weight:[kgs] [{actual_patient.get_weight()}]  ", False, 200, 1)
    actual_patient.set_name(name)
    actual_patient.set_last_name(last_name)
    actual_patient.set_email(email)
    actual_patient.set_gender(gender)
    actual_patient.set_age(age)
    actual_patient.set_height(height)
    actual_patient.set_weight(weight)
    actual_patient.update_modified()


def update_patient():
    for i in range(PATIENTS.size()):
        clean_screen()
        print(PATIENTS.get(i))
        s = input("\n[ u ] To updat\n[ e ] to exit\n_")
        if s == 'u':
            update_patient_form(i)
            print("Done! It was updated.")
            break
        if s == 'e' or i == PATIENTS.size() - 1:
            print("Okay i understand was a mistake")
            break


# DATES METHODS

def validation():
    # validacion de que exista un doctor y un usuario por lo menos
    if PATIENTS.size() == 0 or DOCTORS.size() == 0:
        return False, "Patient or doctors missing\nCannot add with out users.\n SORRY!"

    return True, "All correct!"


def date_form(patient, doctor):
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

    date = Date(get_actual_uid(), doctor, patient,
                date_date, date_time, description)
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


def add_date_end():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    DATES.append(date)
    print("Date added! All Correct")


def show_all_date():
    for i in range(DATES.size()):
        clean_screen()
        print(DATES.get(i))
        s = input("\n[ e ] To exit\n_")
        if s == 'e':
            break


def add_date_begin():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    DATES.preppend(date)
    print("Date added! All Correct")


def insert_date():
    auth = validation()
    if auth[0] is False:
        print(auth[1])
        return

    # seleccionando usuarios
    patient = select_patient()
    doctor = select_doctor()
    clean_screen()
    input("Selection correct! Date Information.")
    date = date_form(patient, doctor)
    idx = input_int("Index to insert: ", False, DATES.size() - 1, 0)
    DATES.insert(date, idx)
    print("Date added! All Correct")


def invert_date():
    DATES.reverse()
    print("The linked list of Dates has been reverse.")
    print("Check it in the [show all dates option]")


def delete_fist_date():
    DATES.shift()
    print("SHIFT! the first Date was deleted.")


def delete_last_date():
    DATES.pop()
    print("POP! The last Date was deleted.")


def remove_date():
    for i in range(DATES.size()):
        clean_screen()
        print(DATES.get(i))
        s = input("\n[ d ] To Delete\n[ e ] to exit\n_")
        if s == 'd':
            DATES.remove(i)
            print("Done! It was deleted.")
            break
        if s == 'e' or i == DATES.size() - 1:
            print("Okay i understand was a mistake")
            break


DATES_OPTIONS = [(1, "Add a Date to the end. [APPEND]", add_date_end),
                 (2, "Add a Date to the begining. [PREPPEND]", add_date_begin),
                 (3, "Insert a Date to a position. [INSERT]", insert_date),
                 (4, "Delete the first Date [SHIFT]", delete_fist_date),
                 (5, "Delete the last Date [POP]", delete_last_date),
                 (6, "Remove a Date in a postition. [REMOVE]"),
                 (7, "Show all the dates. [SHOW]", show_all_date),
                 (8, "Invert the list of dates [INVERT]", invert_date),
                 (9, "Update date Information [UPDATE]"),
                 (9, "Order the list. [ORDER]")
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
    m = Menu(DATES_OPTIONS, 10, False)
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
