#!/usr/bin/python3

class calculator :

	def __add__(self, objet) -> None:
		return (self + objet)

	def __mul__(self, objet) -> None:
		pass

	def __sub__(self, objet) -> None:
		pass

	def __truediv__(self, objet) -> None:
		pass

def main():
	v1 = calculator([0.0, 1.0, 2.0, 3.0, 4.0, 5.0])
	# v1+ 5


if (__name__ == "__main__"):
	main()