

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleListBound:

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def appped(self, val):
        new_node = Node(val)
        if self.__first is None and self.__last is None:
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = self.__last.next
        self.__size += 1

    def last(self):
        return self.__last

    def first(self):
        return self.__first

    def size(self):
        return self.__size

    def __str__(self, node=None, chain="["):
        if node is None:
            # first call time
            node = self.__first
        try:
            chain += '"' + node.data + '"'
        except TypeError as e:
            chain += str(node.data)

        if node.next is None:
            # last element
            chain += "]"
            return chain

        # there are still elements
        chain += ", "

        return self.__str__(node.next, chain)
