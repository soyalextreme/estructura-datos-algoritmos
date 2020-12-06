
from models.User import User


class Person(User):

    def __init__(self, name, last_name, email, uid, gender, age):
        User.__init__(self, name, last_name, email, uid)
        self.__gender = gender
        self.__age = age

    def get_gender(self):
        if self.__gender == 0:
            return "MALE"
        else:
            return "FEMALE"

    def set_gender(self, gender):
        self.__gender = gender

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return User.__str__(self) + f"""
            Age: {self.get_age()} y/old
            Gender: {self.get_gender()}"""
