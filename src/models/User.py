""" 
    USER BASE CLASS

    27-11-2020
    ALejandro AS
"""

from models.Entity import Entity


class User(Entity):

    def __init__(self, name, last_name, email, uid):
        self.__name = name
        self.__last_name = last_name
        self.__email = email
        self.__uid = uid
        Entity.__init__(self)

    def set_name(self, new_name):
        self.__name = new_name

    def get_name(self):
        return self.__name

    def set_last_name(self, new_last_name):
        self.__last_name = new_last_name

    def get_last_name(self):
        return self.__last_name

    def set_email(self, new_email):
        self.__email = new_email

    def get_email(self):
        return self.__email

    def get_uid(self):
        return self.__uid

    def __str__(self):
        chain_desc = f"""
            ========================================================|
            ID: {self.get_uid()}                      
            Name: {self.get_name()}  {self.get_last_name()}
            Email: {self.get_email()}
        """
        return Entity.__str__(self) + chain_desc
