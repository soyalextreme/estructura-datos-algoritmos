from abc import abstractmethod


class Mammal:
    def __init__(self):
        pass

    def breath(self):
        print("Im a mammal I can breath")

    @abstractmethod
    def food(self):
        pass


class Person(Mammal):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.__init__()

    def say_hello(self):
        print(f"{self.name} says: Hellooo!")

    def food(self):
        print("I eat taquitos al pastor")
