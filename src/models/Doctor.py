"""
    DOCTOR MODEL
    
    27-11-2020
    Alejandro AS
"""

from models.Person import Person
from database import DOCTORS
from lib.inputs import input_str_non_empty, input_int
from models.support_functions import select_gender, get_actual_uid


class Doctor(Person):

    def __init__(self, name, last_name, email, uid, gender, age, medical_specialty):
        Person.__init__(self, name, last_name, email, uid, gender, age)
        self.__medical_specialty = medical_specialty

    def get_specialty(self):
        return self.__medical_specialty

    def set_specialty(self, new_specialty):
        self.__medical_specialty = new_specialty

    def __str__(self):
        return Person.__str__(self) + f"""
            Specialty: {self.get_specialty()}
            Role: Doctor
            ================================================|
        """


def create_doctor():
    """
        This function returns a doctor instance.
    """
    name = input_str_non_empty("Doctor Name: ")
    last_name = input_str_non_empty("Doctor Last Name: ")
    email = input_str_non_empty("Doctor Email: ")
    gender = select_gender()
    age = input_int("Doctor Age: ", False, 75, 18)
    medical_specialty = input_str_non_empty("Doctor Specialty: ")
    d = Doctor(name, last_name, email,
               get_actual_uid(), gender, age, medical_specialty)
    return d


def update_doctor(idx):
    """
        Creates and updates the info of a doctor.
    """
    actual_doctor = DOCTORS.get(idx)
    name = input_str_non_empty(f"Doctor Name: [{actual_doctor.get_name()}]  ")

    last_name = input_str_non_empty(
        f"Doctor Last Name: [{actual_doctor.get_last_name()}]  ")

    email = input_str_non_empty(
        f"Doctor Email: [{actual_doctor.get_email()}]  ")

    gender = select_gender()

    age = input_int(f"Doctor Age: [{actual_doctor.get_age()}]  ",
                    False, 75, 18, default=actual_doctor.get_age())

    medical_specialty = input_str_non_empty(
        f"Doctor Specialty: [{actual_doctor.get_specialty()}]  ")

    d = Doctor(name, last_name, email,
               actual_doctor.get_uid(), gender, age, medical_specialty)

    d.set_created(actual_doctor.get_created())
    d.update_modified()
    return d
