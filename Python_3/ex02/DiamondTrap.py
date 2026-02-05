#!/usr/bin/python3

from S1E7 import Baratheon, Lannister

class King(Baratheon, Lannister):
	"""
Docstring for King
Child of Baratheon and Lannister.
Diamond inheritance : python uses C3 linearization to decide the order.
This order is called MRO (method resolution order)
The order will always be King -> Baratheon -> Lannister -> Character -> Object
	"""
	def __init__(self, first_name, is_alive = True):
		super().__init__(first_name, is_alive = True)
	
	def set_eyes(self, newEyes):
		self.eyes = newEyes
	
	def set_hairs(self, newHairs):
		self.hairs = newHairs

	def get_eyes(self):
		return (self.eyes)
	
	def get_hairs(self):
		return (self.hairs)


def main():
	Joffrey = King("Joffrey")
	print(Joffrey.__dict__)
	Joffrey.set_eyes("blue")
	# print(Joffrey.__dict__)
	Joffrey.set_hairs("light")
	print(Joffrey.get_eyes())
	print(Joffrey.get_hairs())
	print(Joffrey.__dict__)

	print(King.mro())

if (__name__ == "__main__"):
	main()