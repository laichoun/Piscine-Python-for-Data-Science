#!/usr/bin/python3
from abc import ABC, abstractmethod

class Character(ABC):
	"""
	Class Character
	"""
	print("test1")

class Stark(Character):
	print("test")


def main():
	p1 = Character()


if (__name__ == "__main__"):
	main()