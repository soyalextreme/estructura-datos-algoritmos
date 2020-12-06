from lib.menu import MenuOptions
import uuid


def select_gender():
    op = ["Male", "Female"]
    m = MenuOptions(op)
    return m.select()


def get_actual_uid():
    return uuid.uuid1()
