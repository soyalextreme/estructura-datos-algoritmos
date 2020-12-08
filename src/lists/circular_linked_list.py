"""

    Circular Linked List

    30-11-2020
    ALejandro AS
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:

    def __init__(self):
        self.__first = None
        self.__last = None

    def append(self, val):
        """
            Adds a element at the end of the list.
        """
        node = Node(val)
        if self.__first is None and self.__last is None:
            self.__last = node
            self.__first = node
        else:
            self.__last.next = node
            node.next = self.__first
            self.__last = node

    def preppend(self, val):
        """
            Adds a element at the begining of the list.
        """
        node = Node(val)
        if self.__first is None and self.__last is None:
            self.__last = node
            self.__first = node
        else:
            node.next = self.__first
            self.__first = node
            self.__last.next = self.__first

    def __get_node(self, idx):
        if idx > self.size() - 1 or idx < 0:
            raise IndexError
        node = self.__first
        for _ in range(idx):
            node = node.next
        return node

    def get(self, idx):
        """
            Returns the value of a index
        """

        if idx > self.size() - 1 or idx < 0:
            raise IndexError

        node = self.__first
        for _ in range(idx):
            node = node.next
        return node.data

    def insert(self, val, idx):
        """
            Inserts a element before the position of the list
        """
        if idx > self.size() - 1 or idx < 0:
            raise IndexError

        if self.size() == 0 or self.size() - 1 == idx:
            self.append(val)
            return True

        new_node = Node(val)
        node = self.__get_node(idx)
        temp = node.next
        new_node.next = temp
        node.next = new_node

    def update(self, val, idx):
        node_update = self.__get_node(idx)
        node_update.data = val

    def preinstert(self, val, idx):
        """
            Add a element to the index in the prev position.
        """
        if idx > self.size() - 1 or idx < 0:
            raise IndexError

        if idx == 0 or self.size() == 0:
            return self.preppend(val)

        new_node = Node(val)
        node_prev = self.__get_node(idx - 1)
        new_node.next = node_prev.next
        node_prev.next = new_node

    def shift(self):
        """
            Deletes the first element of the list.
        """
        if self.size() == 0:
            return

        if self.size() == 1:
            self.__first = None
            self.__last = None
            return

        temp = self.__first.next
        self.__first.next = None
        val = self.__first.data
        self.__first = temp
        self.__last.next = self.__first
        return val

    def pop(self):
        """
            Removes the las element of the list.
        """
        if self.size() == 1:
            self.__last = None
            self.__first = None
            return

        if self.size() == 0:
            return

        last_prev = self.__get_node(self.size() - 2)
        last_prev.next = self.__first
        val = self.__last.data
        self.__last.next = None
        self.__last = last_prev
        return val

    def remove(self, idx):
        """
            Removes a element in a determine position.
        """
        if idx > self.size() - 1 or idx < 0:
            raise IndexError

        if idx == 0:
            return self.shift()
        elif idx == self.size() - 1:
            return self.pop()

        node_prev = self.__get_node(idx - 1)
        node_next = node_prev.next.next
        node_del = node_prev.next
        node_prev.next = node_next
        node_del.next = None
        return node_del.data

    def size(self):
        """
            Returns the size of the list.
        """
        size = 0
        node = self.__first
        if node is None:
            return size

        while True:
            size += 1
            if node.next == None or node.next == self.__first:
                break
            node = node.next
        return size

    def reverse(self):
        """
            Reverse the linked list.
        """
        if self.__first == None or self.size() == 1:
            return

        node = self.__first
        next_nodes = node
        prev = None
        next_nodes = next_nodes.next
        node.next = prev
        prev = node
        node = next_nodes

        while node != self.__first:
            next_nodes = next_nodes.next
            node.next = prev
            prev = node
            node = next_nodes
        node.next = prev
        self.__first = prev

    def copy(self):
        """
            Returns a copy of the linked list with different pointer.
        """
        copy = CircularLinkedList()
        for i in range(self.size()):
            val_node = self.get(i)
            copy.append(val_node)
        return copy

    def clear(self):
        self.__first = None
        self.__last = None

    def __str__(self):
        node = self.__first
        chain = "["

        if node == None:
            return chain + "]"

        while True:
            if type(node.data) == str:
                chain += f'"{node.data}", '
            else:
                chain += str(node.data) + ", "
            node = node.next

            try:
                if node.next == self.__first:
                    if type(node.data) == str:
                        chain += f'"{node.data}"'
                    else:
                        chain += str(node.data)
                    break
            except AttributeError as e:
                return chain + "]"
        return chain + "]"


if __name__ == "__main__":
    # cd = CircularLinkedList()
    # # cd.append(10)
    # # cd.append(20)
    # # cd.preppend(2)
    # # cd.preppend(1)
    # # cd.preppend(100)
    # # cd.append("alex")
    # # cd.preppend("juanito")
    # # cd.insert("holis", 2)
    # # cd.preinstert("ahhahah", 1)
    # # print(cd.shift())
    # # print(cd.shift())
    # # print(cd.pop())
    # # print(cd.remove(2))
    # # print(cd.remove(2))
    # # print(cd)
    # # print(cd.reverse())
    # # print(cd.size())

    # cd = CircularLinkedList()
    # cd.append("hola")
    # cd.remove(0)
    # cd.append("hola")
    # cd.append("como estas")
    # cd.append("como estas")
    # cd.append("como estas")
    # cd.append("como estas")
    # cd.append("como estas")
    # print(cd)
    # print(cd.size())
    # cd = CircularLinkedList()
    # cd.append(0)
    # print(cd)
    # cd.update("como estas", 0)
    # print(cd)
    pass
