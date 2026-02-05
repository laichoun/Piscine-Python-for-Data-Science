#!/usr/bin/python3

from S1E9 import Character


class Baratheon(Character):
    """Docstring for Baratheon : Representing the Baratheon family.
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        self.is_alive = False

    def __repr__(self):
        return (f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")

    def __str__(self):
        return (self.__repr__())


class Lannister(Character):
    """Docstring for Lannister : Creation of Lannister class

    @classmethod is bound to the class and not to an instance of the class
    """
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        self.is_alive = False

    def __repr__(self):
        return (f"Vector: ({self.family_name}, {self.eyes}, {self.hairs})")

    def __str__(self):
        return (self.__repr__())

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        return cls(first_name, is_alive)


def main():
    Robert = Baratheon("Robert")
    print(Robert.__dict__)
    print(Robert.__str__)
    print(Robert.__repr__)
    print(Robert.is_alive)
    Robert.die()
    print(Robert.is_alive)
    print(Robert.__doc__)
    print("<=============================================>")
    Cersei = Lannister("Cersei")
    print(Cersei.__dict__)
    print(Cersei.__str__)
    print(Cersei.is_alive)

    print("<=============================================>")
    Jaine = Lannister.create_lannister("Jaine", True)
    print(f"Name :{Jaine.first_name, type(Jaine).__name__}, Alive : {Jaine.is_alive}")


if (__name__ == "__main__"):
    main()
