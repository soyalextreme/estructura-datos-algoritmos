import datetime
import pickle


class Entity:

    def __init__(self):
        date = datetime.datetime.now()
        self.__created = date
        self.__modified = datetime.datetime.now()

    def update_modified(self):
        self.__modified = datetime.datetime.now()

    def set_created(self, new):
        self.__created = new

    def get_created(self):
        return self.__created

    def __str__(self):
        chain_desc = f"""
            ========================================================|
            Created: {self.__created}
            Modified: {self.__modified}
        """
        return chain_desc
