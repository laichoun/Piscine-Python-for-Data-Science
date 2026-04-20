#!/usr/bin/python3

import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """
Dataclass is a decorator that permits generate automatically the functions
needed to create an object as __init__, __repr__, __str__. More readable.

Field is a function that permits to put rules. : remove the variable from
the constructor, display it with repr.etc.
Field takes several parameters :
    - default= to put a value as default
    - default_factory is a function that is called at each instance creation

__post_init__ is called right after the __init__ method to do more operations.
It is used to compute or adjust fields after initialization
when all instance attributes are already available
    """
    name: str
    surname: str
    active: bool = field(default=True, init=False)
    id: str = field(init=False, default_factory=generate_id)
    login: str = field(init=False)

    def __post_init__(self):
        self.login = self.name[:1] + self.surname[:7]


def main():
    student = Student("Lalla", surname="Aichouni")
    student2 = Student(name="Edward", surname="agle")
    student3 = Student(name="Edward", surname="agle")
    student4 = Student(name="Edward", surname="agle")
    student5 = Student(name="Edward", surname="agle")
    student6 = Student(name="Edward", surname="agle")
    print(student)
    print(student2)
    print(student3)
    print(student4)
    print(student5)
    print(student6)


if (__name__ == "__main__"):
    main()
