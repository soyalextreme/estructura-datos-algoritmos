"""
    Patient CRUD methods.

    ADD
    DELETE 
    UPDATE
    SHOW
"""

from models.Patient import Patient
from lib.inputs import input_str_non_empty, input_int, input_float
from models.support_functions import select_gender, get_actual_uid
from database import PATIENTS, DATES
from lib.util import clean_screen
from database import save_changes


@save_changes
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
    input(f"Congrats!!! Patient {name} Added Successfully")
    return True


def show_all_patient():
    if PATIENTS.size() == 0:
        print("Empty! No patient to show.")
        return

    for i in range(PATIENTS.size()):
        clean_screen()
        print(PATIENTS.get(i))
        s = input("\n[ e ] To exit\n_")
        if s == 'e':
            break


def search_dates_patient_id(i):
    patient_to_del = PATIENTS.get(i)
    uid = patient_to_del.get_uid()
    founded = False
    for i in range(DATES.size()):
        date = DATES.get(i)
        if date.get_patient().get_uid() == uid:
            DATES.remove(i)
            founded = True
    if founded:
        print("Dates of the patient deleted.")
    else:
        print("No dates linked to the patient.")


@save_changes
def delete_patient():
    if PATIENTS.size() == 0:
        print("Empty! No patient to delete.")
        return

    delted = False
    for i in range(PATIENTS.size()):
        clean_screen()
        print(PATIENTS.get(i))
        s = input("\n[ d ] To Delete\n[ e ] to exit\n_")
        if s == 'd':
            # search_dates_patient_id(i)
            PATIENTS.remove(i)
            input("Done! It was deleted.")
            delted = True
            break
        if s == 'e' or i == PATIENTS.size() - 1:
            print("Okay i understand was a mistake")
            break
    return delted


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
    symptoms = input_str_non_empty(
        f"Patient Symptoms: [{actual_patient.get_symptoms()}]  ")
    actual_patient.set_name(name)
    actual_patient.set_last_name(last_name)
    actual_patient.set_email(email)
    actual_patient.set_gender(gender)
    actual_patient.set_age(age)
    actual_patient.set_height(height)
    actual_patient.set_weight(weight)
    actual_patient.set_symptoms(symptoms)
    actual_patient.update_modified()


def update_dates_from_patient(i):
    uid = PATIENTS.get(i).get_uid()
    updated = False
    for j in range(DATES.size()):
        date = DATES.get(j)
        if date.get_patient().get_uid() == uid:
            date.set_patient(PATIENTS.get(i))
            updated = True
    if updated:
        print("Dates of this patient were modified.")


@save_changes
def update_patient():
    if PATIENTS.size() == 0:
        print("Empty! No patient do update.")
        return False

    updated = False
    for i in range(PATIENTS.size()):
        clean_screen()
        print(PATIENTS.get(i))
        s = input("\n[ u ] To update\n[ e ] to exit\n_")
        if s == 'u':
            update_patient_form(i)
            update_dates_from_patient(i)
            input("Done! It was updated.")
            updated = True
            break
        if s == 'e' or i == PATIENTS.size() - 1:
            print("Okay i understand was a mistake")
            break
    return updated
