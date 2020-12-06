import pickle

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

    with open("DATABASE.txt", "wb") as fp:
        pickle.dump(database, fp)


def load():

    with open("DATABASE.txt", "rb") as fp:
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
