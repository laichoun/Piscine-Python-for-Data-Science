#!/usr/bin/python3
from abc import ABC, abstractmethod


class Character(ABC):
    """
Class Character : Abstract class because its
parent is ABC and has a abstractmethod
It has a constructor init and an abstract methode die()
    """
    def __init__(self, first_name, is_alive = True):
        """
Docstring for __init__ the constructor
        
:param self: Description for the object itself
:param first_name
:param is_alive
        """
        self.first_name = first_name
        self.is_alive = is_alive


    @abstractmethod
    def die(isAlive):
        pass


class Stark(Character):
    """
Class Stark : child of Character
    """
    def __init__(self, first_name, is_alive=True):
        """
Docstring for __init__ : Takes the constructor of the parent

:param self: Description
:param first_name: Description
:param is_alive: Description
        """
        super().__init__(first_name, is_alive)


    def die(self):
        """
Docstring for die

Change the state of is_alive
        """
        self.is_alive = False


def main():
    Ned = Stark("Ned")
    print(Ned.__dict__)
    print(Ned.is_alive)
    Ned.die()
    print(Ned.is_alive)
    print(Ned.__doc__)
    print(Ned.__init__.__doc__)
    print(Ned.die.__doc__)
    print("---")
    Lyanna = Stark("Lyanna", False)
    print(Lyanna.__dict__)
    # hodor = Character("hodor")


if (__name__ == "__main__"):
    main()