"""
    Binary Search Three

    04-12-2020
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.l = None
        self.r = None


class BinarySearchTree:

    def __init__(self):
        self.__root = None

    def insert(self, val):
        new_node = Node(val)
        if self.__root == None:
            self.__root = new_node
            return True
        else:
            def check(val, node):
                if val == node.val:
                    return "ya existe"
                if val < node.val:
                    if node.l == None:
                        node.l = new_node
                        return True
                    else:
                        return check(val, node.l)
                if val > node.val:
                    if node.r == None:
                        node.r = new_node
                        return True
                    else:
                        return check(val, node.r)

            check(val, self.__root)

    def innorder(self, node=None, l=None, first_it=True):
        if first_it == True:
            node = self.__root
            l = []

        if node == None:
            return
        else:
            self.innorder(node.l, l, False)
            l.append(node.val)
            self.innorder(node.r, l, False)
            return l

    def preorder(self, node=None, l=None, first_it=True):
        if first_it == True:
            node = self.__root
            l = []

        if node == None:
            return None
        else:
            l.append(node.val)
            self.preorder(node.l, l, False)
            self.preorder(node.r, l, False)
            return l

    def postorder(self, node=None, l=None, first_it=True):
        if first_it == True:
            node = self.__root
            l = []

        if node == None:
            return None
        else:
            self.postorder(node.l, l, False)
            self.postorder(node.r, l, False)
            l.append(node.val)
            return l

    def find(self, val, node=False):
        """
            Finds a element in the list recursive
        """
        if node == False:
            node = self.__root
        if node == None:
            return False
        elif node.val == val:
            return True
        else:
            if node.val > val:
                return self.find(val, node.l)
            elif node.val < val:
                return self.find(val, node.r)

    def find_successor(self, node):
        while node.l != None:
            node = node.l
        return node

    def delete(self, val):
        father = None
        node = self.__root

        try:
            while node.val != val:
                father = node

                if val < node.val:
                    node = node.l
                else:
                    node = node.r
        except AttributeError as e:
            return "not founded"

        if node == None:
            return "Not founded"

        # case that the node to delete has no children
        if node.l == None and node.r == None:

            if node != self.__root:
                if father.l == node:
                    father.l = None
                else:
                    father.r = None
            else:
                self.__root = None
        # case the node has both children
        if node.l and node.r:
            successor = self.find_successor(node.r)
            val = successor.val

            self.delete(successor.val)
            # asignamos el valor al node que vamos a elminar
            node.val = val

        # case 3 the node only has one children
        else:
            if node.l:
                child_from_del = node.l
            else:
                child_from_del = node.r

            if node != self.__root:
                if node == father.l:
                    father.l = child_from_del
                else:
                    father.r = child_from_del
            else:
                self.__root = child_from_del
        return "Borrado Correctamente"


class BinarySearchTreeAdapted:

    def __init__(self):
        self.__root = None

    def insert(self, val):
        new_node = Node(val)
        if self.__root == None:
            self.__root = new_node
            return True
        else:
            def check(val, node):
                if val[0] == node.val[0]:
                    return "ya existe"
                if val[0] < node.val[0]:
                    if node.l == None:
                        node.l = new_node
                        return True
                    else:
                        return check(val, node.l)
                if val[0] > node.val[0]:
                    if node.r == None:
                        node.r = new_node
                        return True
                    else:
                        return check(val, node.r)

            check(val, self.__root)

    def innorder(self, node=None, l=None, first_it=True):
        if first_it == True:
            node = self.__root
            l = []

        if node == None:
            return
        else:
            self.innorder(node.l, l, False)
            l.append(node.val)
            self.innorder(node.r, l, False)
            return l

    def preorder(self, node=None, l=None, first_it=True):
        if first_it == True:
            node = self.__root
            l = []

        if node == None:
            return None
        else:
            l.append(node.val)
            self.preorder(node.l, l, False)
            self.preorder(node.r, l, False)
            return l

    def postorder(self, node=None, l=None, first_it=True):
        if first_it == True:
            node = self.__root
            l = []

        if node == None:
            return None
        else:
            self.postorder(node.l, l, False)
            self.postorder(node.r, l, False)
            l.append(node.val)
            return l

    def find(self, val, node=False):
        """
            Finds a element in the list recursive
        """
        if node == False:
            node = self.__root
        if node == None:
            return "Not founded"
        elif node.val[0] == val:
            return node.val[1]
        else:
            if node.val[0] > val:
                return self.find(val, node.l)
            elif node.val[0] < val:
                return self.find(val, node.r)

    def find_successor(self, node):
        while node.l != None:
            node = node.l
        return node

    def delete(self, val):
        father = None
        node = self.__root

        try:
            while node.val[0] != val:
                father = node

                if val < node.val[0]:
                    node = node.l
                else:
                    node = node.r
        except AttributeError as e:
            return "not founded"

        if node == None:
            return "Not founded"

        # case that the node to delete has no children
        if node.l == None and node.r == None:
            if node != self.__root:
                if father.l == node:
                    father.l = None
                else:
                    father.r = None
            else:
                self.__root = None
        # case the node has both children
        elif node.l and node.r:
            successor = self.find_successor(node.r)
            val = successor.val

            self.delete(successor.val)
            # asignamos el valor al node que vamos a elminar
            node.val = val

        # case 3 the node only has one children
        else:
            if node.l:
                child_from_del = node.l
            else:
                child_from_del = node.r

            if node != self.__root:
                if node == father.l:
                    father.l = child_from_del
                else:
                    father.r = child_from_del
            else:
                self.__root = child_from_del
        return "Deleted Okay"
