"""
    Class Date for appointments

    Alejandro AS
    04-12-2020
"""


class Date:

    def __init__(self, uid, doctor, patient, date, time, description):
        self.__uid = uid
        self.__doctor = doctor
        self.__patient = patient
        self.__description = description
        self.__time = time
        self.__date = date

    def get_uid(self):
        return self.__uid

    def get_description(self):
        return self.__description

    def set_description(self, new):
        self.__description = new

    def set_time(self, new):
        self.__time = new

    def get_time(self):
        return self.__time

    def get_date(self):
        return self.__date

    def set_date(self, new):
        self.__date = new

    def __str__(self):
        return f"""
            Date ID: {self.get_uid()}
            Date: {self.get_date()} {self.get_time()} 
            Description: {self.get_description()}
            ====================================================
            Patient Name: {self.__patient.get_name()}
            Patient ID: {self.__patient.get_uid()}
            Patient Symptoms: {self.__patient.get_symptoms()}
            ====================================================
            Doctor Name: {self.__doctor.get_name()}
            Doctor ID: {self.__doctor.get_uid()}
            Doctor Specialty: {self.__doctor.get_specialty()}
        """
