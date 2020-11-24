

class Node:

    def __init__(self, value):
        self.__value = value
        self.__next = None
        self.__prev = None

    def getNext(self):
        return self.__next

    def setNext(self, new_next):
        self.__next = new_next

    def getPrev(self):
        return self.__prev

    def setPrev(self, new_prev):
        self.__prev = new_prev

    def getVal(self):
        return self.__value

    def setVal(self, new_value):
        self.__value = new_value


class DoubleLinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None

    def append(self, val):
        """ 
            Appends a element at the end of the list
        """
        new_node = Node(val)
        last = self.__last
        first = self.__first
        if first is None and last is None:
            self.__first = new_node
            self.__last = new_node
            return

        self.__last.setNext(new_node)
        new_node.setPrev(last)
        self.__last = new_node

    def get(self, idx):
        """
            Gets the value of the index corresponding 
        """
        if idx == 0:
            return self.__first.getVal()
        elif idx == self.size() - 1:
            return self.__last.getVal()

        node = self.__first
        for _ in range(0, idx):
            node = node.getNext()

        return node.getVal()

    def __get_node(self, idx):
        """
            Gets the node corresponding to the index
        """
        if idx == 0:
            return self.__first
        elif idx == self.size() - 1:
            return self.__last

        node = self.__first
        for _ in range(0, idx):
            node = node.getNext()

        return node

    def pop(self):
        """ 
            Deletes the last element of the list
        """
        if self.size() > 1:
            prev = self.__last.getPrev()
            prev.setNext(None)
            self.__last.setPrev(None)
            self.__last = prev
        else:
            self.shift()

    def shift(self):
        """
            Deletes the first element of the list
        """

        if self.size() == 1:
            self.__first = None
            self.__last = None
        elif self.size() == 0:
            return
        else:
            temp_first = self.__first
            self.__first = temp_first.getNext()
            self.__first.setPrev(None)
            temp_first.setNext(None)

    def prepend(self, val):
        """
            Insert a element at the first position of the list
        """
        temp_first = self.__first
        new_node = Node(val)
        temp_first.setPrev(new_node)
        new_node.setNext(temp_first)
        self.__first = new_node

    def remove(self, idx):
        """
             Deletes a element of the list with the index.
        """
        if idx == 0:
            return self.shift()
        elif idx == self.size() - 1:
            return self.pop()

        node_to_delete = self.__get_node(idx)
        node_to_delete.getPrev().setNext(node_to_delete.getNext())
        node_to_delete.getNext().setPrev(node_to_delete.getPrev())
        node_to_delete.setPrev(None)
        node_to_delete.setNext(None)

    def update(self, idx, val):
        """
            Updates the value of the position of a element
        """
        if self.size() > 0 and idx <= self.size() - 1 and idx >= 0:
            node = self.__get_node(idx)
            node.setVal(val)
        else:
            return None

    def insert(self, idx, val):
        """
            Insert before the value of the index.
        """
        if self.size() > 0 and idx <= self.size() - 1 and idx >= 0:
            node = self.__get_node(idx)
            new_node = Node(val)
            temp_next = node.getNext()
            node.setNext(new_node)
            new_node.setPrev(node)
            new_node.setNext(temp_next)

    def preinsert(self, idx, val):
        new_node = Node(val)
        if idx == 0:
            temp_first = self.__first
            self.__first = new_node
            new_node.setNext(temp_first)
            temp_first.setPrev(new_node)

        if self.size() > 0 and idx <= self.size() - 1 and idx >= 0:
            node = self.__get_node(idx - 1)
            temp_next = node.getNext()
            node.setNext(new_node)
            new_node.setPrev(node)
            new_node.setNext(temp_next)
            temp_next.setPrev(new_node)

    def clear(self):
        """
            This method clears and deletes all the elements in the list
        """
        self.__first = None
        self.__last = None

    def reverse(self, node=None, l=None):
        """
            Returns a copy of the list but inverted
        """
        if l is None:
            node = self.__last
            l = DoubleLinkedList()

        l.append(node.getVal())

        if node.getPrev() is None:
            return l

        return self.reverse(node.getPrev(), l)

    def copy(self):
        """
            Returns a copy of the list with different memory location for usage.
        """
        l_copy = DoubleLinkedList()
        node = self.__first
        for _ in range(self.size()):
            l_copy.append(node.getVal())
            node = node.getNext()

        return l_copy

    def size(self, node=None, size=0):
        if self.__first is None:
            return 0

        if node is None and self.__first is not None:
            node = self.__first

        size += 1

        if node.getNext() is None:
            return size

        return self.size(node.getNext(), size)

    def __str__(self, node=None, chain="["):
        if node is None:
            # first call time
            node = self.__first
            if self.__first is None:
                return "[ ]"

        try:
            chain += '"' + node.getVal() + '"'
        except TypeError as e:
            chain += str(node.getVal())

        if node.getNext() is None:
            # last element
            chain += "]"
            return chain

        # there are still elements
        chain += ", "

        return self.__str__(node.getNext(), chain)
