import random


class Nodo:
    def __init__(self, dato):
        super().__init__()
        self.dato = dato
        self.siguiente = None


class ListaLigadaSimple:
    def __init__(self):
        super().__init__()
        self.primero = None
        self.ultimo = None
        self.tamaño = 0

    def append(self, dato):
        nuevoNodo = Nodo(dato)
        if self.primero == None and self.ultimo == None:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            self.ultimo.siguiente = nuevoNodo
            self.ultimo = nuevoNodo
            #self.ultimo = self.ultimo.siguiente
        self.tamaño += 1

    def prepend(self, dato):
        nuevoNodo = Nodo(dato)
        if self.primero == None and self.ultimo == None:
            self.primero = nuevoNodo
            self.ultimo = nuevoNodo
        else:
            nuevoNodo.siguiente = self.primero
            self.primero = nuevoNodo
        self.tamaño += 1

    # Eliminar el primero
    def shift(self):
        if self.tamaño != 0:
            nodoEliminado = self.primero
            self.primero = self.primero.siguiente
            nodoEliminado.siguiente = None
            self.tamaño -= 1
            return nodoEliminado.dato

    # Eliminar el último
    def pop(self):
        if self.tamaño != 0:
            nodoActual = self.primero
            nuevoUltimo = nodoActual
            while nodoActual.siguiente != None:
                nuevoUltimo = nodoActual
                nodoActual = nodoActual.siguiente
            self.ultimo = nuevoUltimo
            self.ultimo.siguiente = None
            self.tamaño -= 1
            return nodoActual.dato

    def get(self, indice):
        if indice == self.tamaño-1:
            return self.ultimo
        elif indice == 0:
            return self.primero
        elif not(indice >= self.tamaño or indice < 0):
            nodoActual = self.primero
            contador = 0
            while contador != indice:
                nodoActual = nodoActual.siguiente
                contador += 1
            return nodoActual
        else:
            return None

    def update(self, indice, dato):
        nodoObjetivo = self.get(indice)
        if nodoObjetivo != None:
            nodoObjetivo.dato = dato

    def __str__(self):
        nodoActual = self.primero
        l = []
        while nodoActual != None:
            # print(nodoActual.dato)
            l.append(nodoActual.dato)
            nodoActual = nodoActual.siguiente
        return str(l)


def bubble_sort(l):
    n = l.tamaño
    for i in range(n):
        for j in range(n - i - 1):
            if l.get(j).dato > l.get(j + 1).dato:
                key = l.get(j).dato
                l.update(j, l.get(j + 1).dato)
                l.update(j + 1, key)


def main():
    n = int(input("Tamano de tu lista: "))
    l = ListaLigadaSimple()
    for i in range(n):
        n = random.randint(-100, 100)
        l.append(n)
    print(l)
    bubble_sort(l)
    print(l)


main()
