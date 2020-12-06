"""
    Stack Data structure 

    30-11-2020
    Alejandro AS
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Stack:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def push(self, data):
        new_node = Node(data)
        if self.__first is None and self.__last is None:
            self.__last = new_node
            self.__first = new_node
        else:
            new_node.next = self.__first
            self.__first = new_node

        self.__size += 1

    def pop(self):
        if self.__first is not None:
            deleted_node = self.__first
            self.__first = self.__first.next
            deleted_node.next = None
            self.__size -= 1
            return deleted_node.data

    def peek(self):
        return self.__first.val
