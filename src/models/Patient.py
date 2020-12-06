"""
    PATIENT MODEL
    
    27-11-2020
    Alejandro AS
"""

from models.Person import Person


class Patient(Person):

    def __init__(self, name, last_name, email, uid, gender, age, height, weight, symptoms):
        Person.__init__(self, name, last_name, email, uid, gender, age)
        self.__age = age
        self.__height = height
        self.__weight = weight
        self.__symptoms = symptoms

    def get_age(self):
        return (self.__age)

    def set_age(self, new_age):
        self.__age = new_age

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_symptoms(self):
        return self.__symptoms

    def set_symptoms(self, symptoms):
        self.__symptoms = symptoms

    def __str__(self):
        chain_desc = f"""
            Height:  {self.get_height()} mts.
            Weight: {self.get_weight()} kgs.
            Symptoms: {self.get_symptoms()}
            Role: Patient
            ==========================================================
        """
        return Person.__str__(self) + chain_desc
