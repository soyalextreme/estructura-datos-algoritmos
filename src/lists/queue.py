"""
    Queue Data Structure 

    30-11-2020
    Alejandro AS
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def enqueue(self, val):
        new_node = Node(val)
        if self.__first is None and self.__last is None:
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = self.__last.next
        self.__size += 1

    def dequeue(self):
        if self.__first is not None:
            deleted_node = self.__first
            self.__first = self.__first.next
            deleted_node.next = None
            self.__size -= 1
            return deleted_node.data

    def __str__(self, node=None, chain="["):
        if node is None:
            # first call time
            node = self.__first
            if self.__first is None:
                return "[ ]"

        try:
            chain += '"' + node.val + '"'
        except TypeError as e:
            chain += str(node.val)

        if node.next is None:
            # last element
            chain += "]"
            return chain

        # there are still elements
        chain += ", "

        return self.__str__(node.next, chain)
