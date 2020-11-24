

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SimpleLinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None
        self.__size = 0

    def append(self, val):
        new_node = Node(val)
        if self.__first is None and self.__last is None:
            self.__first = new_node
            self.__last = new_node
        else:
            self.__last.next = new_node
            self.__last = self.__last.next
        self.__size += 1

    def last(self):
        try:
            return self.__last.data
        except AttributeError as e:
            return None

    def first(self):
        try:
            return self.__first.data
        except AttributeError as e:
            return None

    def size(self):
        return self.__size

    def get(self, idx, count=0, node=None):
        self.__val_index(idx)
        if idx == 0:
            return self.__first.data

        if idx == self.size() - 1:
            return self.__last.data

        if node is None:
            node = self.__first

        if idx == count:
            return node.data
        count += 1
        return self.get(idx, count, node.next)

    def get_node(self, idx, count=0, node=None):
        self.__val_index(idx)
        if idx == 0:
            return self.__first
        if idx == self.size() - 1:
            return self.__last
        if node is None:
            node = self.__first
        if idx == count:
            return node
        count += 1
        return self.get(idx, count, node.next)

    def shift(self):
        if self.__first is not None:
            deleted_node = self.__first
            self.__first = self.__first.next
            deleted_node.next = None
            self.__size -= 1
            return deleted_node.data

    def pop(self, idx=None, count=0, node=None):
        if node is None:
            node = self.__first

        if idx is None:
            idx = self.size() - 2

        if idx == 0 or self.size() - 1 == 0:
            self.shift()
            return

        if idx < 0:
            return "Index out of range"

        if idx == count:
            last = node.next
            almost_last = node
            if last.next is None:
                almost_last.next = None
            else:
                almost_last.next = last.next
                last.next = None
            self.__size -= 1
            return last.data
        count += 1
        return self.pop(idx, count, node.next)

    def update(self, idx, data, count=0, node=None):
        self.__val_index(idx)

        if node is None:
            node = self.__first
        if count == idx:
            node.data = data
            return "All changes done"

        count += 1
        return self.update(idx, data, count, node.next)

    def prepend(self, data):
        new_node = Node(data)
        if self.__first is None and self.__last is None:
            self.__last = new_node
            self.__first = new_node
        else:
            new_node.next = self.__first
            self.__first = new_node

        self.__size += 1

    def copy(self, node=False, l=None):
        if node is False:
            node = self.__first

        if l is None:
            l = SimpleLinkedList()

        l.append(node.data)

        if self.__first is None or node.next is None:
            return l

        return self.copy(node=node.next, l=l)

    def insert(self, idx, val):
        self.__val_index(idx)
        new_node = Node(val)
        if self.__first is None:
            self.__first = new_node
            self.__last = new_node
        else:
            actual_node = self.get_node(idx)
            new_node.next = actual_node.next
            actual_node.next = new_node
        self.__size += 1

    def reverse(self):
        l_reverse = SimpleLinkedList()
        for i in range(self.size() - 1, -1, -1):
            node = self.get(i)
            l_reverse.append(node)
        return l_reverse

    def __val_index(self, idx):
        if idx > self.size() - 1 or idx < 0:
            raise IndexError

    def __str__(self, node=None, chain="["):
        if node is None:
            # first call time
            node = self.__first
            if self.__first is None:
                return "[ ]"

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
