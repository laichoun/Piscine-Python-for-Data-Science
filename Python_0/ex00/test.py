nb1 = input("entrez le premier nombre : ")

nb2 = input("entrez le deuxième nombre : ")

print(nb1, nb2)

if nb1.isnumeric() and nb2.isnumeric() :
	nbr1 = int(nb1)
	nbr2 = int(nb2)
else : 
	print("not numbers !!!!")
	raise SystemExit("Fin du programme")

operation = input("Which operation do you want to do ? + - * / : ")
if operation != "+" and operation != "-" and operation != "*" and operation != "/" :
	raise SystemExit("Fin du programme")

match operation:
	case "+":
		result = nbr1 + nbr2
	case "-":
		result = nbr1 - nbr2
	case "*":
		result = nbr1 * nbr2
	case "/":
		if nbr2 == 0 :
			raise SystemExit("Fin du programme, division par 0 impossible")
		result = nbr1 / nbr2
	case _:
		print("impossible operator does not exist")

print(result)



# private test : 
plateformes_sociales = {"Facebook" : "fb", "Instagram" : "insta", "Snapchat" : "snap", "Twitter" : "tweet", 12 : 120}
print(plateformes_sociales)
print (plateformes_sociales.keys())
print (plateformes_sociales.values())
print (plateformes_sociales.items())
print (plateformes_sociales.get("Instagram"))
# print (plateformes_sociales.pop("11"))
print (plateformes_sociales.pop(12))
print(plateformes_sociales)
print (plateformes_sociales.clear())
print(plateformes_sociales)

