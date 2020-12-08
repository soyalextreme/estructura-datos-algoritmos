import pickle
import os
from lists.circular_linked_list import CircularLinkedList
from lists.binary_tree import BinarySearchTreeAdapted as BinarySearchTree


DOCTORS = CircularLinkedList()
PATIENTS = CircularLinkedList()
DATES = CircularLinkedList()
DOCTORS_TREE = BinarySearchTree()


def save():

    d = []
    for i in range(DOCTORS.size()):
        d.append(DOCTORS.get(i))

    p = []
    for i in range(PATIENTS.size()):
        p.append(PATIENTS.get(i))

    da = []
    for i in range(DATES.size()):
        da.append(DATES.get(i))

    database = [d, p, da]

    with open(".DATABASE.txt", "wb") as fp:
        pickle.dump(database, fp)


def load():
    DOCTORS.clear()
    PATIENTS.clear()
    DATES.clear()
    try:
        with open(".DATABASE.txt", "rb") as fp:
            try:
                database = pickle.load(fp)

                d = database[0]
                p = database[1]
                da = database[2]

                for doc in d:
                    DOCTORS.append(doc)

                for patient in p:
                    PATIENTS.append(patient)

                for date in da:
                    DATES.append(date)

            except EOFError as e:
                input("Empty DB")

    except FileNotFoundError as e:
        input("Creating a file .DATABASE.txt")
        os.system("touch .DATABASE.txt")


def save_changes(func):
    def wrapper(*args, **kwargs):
        changes = func()
        save()
        load()
        if changes:
            for i in range(10):
                from lib.util import clean_screen
                clean_screen()
                print("SAVING AND LOADING CHANGES")
                print("=" * i * 5)
                from time import sleep
                sleep(0.3)
        return None
    return wrapper
