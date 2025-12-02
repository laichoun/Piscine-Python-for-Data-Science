nombres = input ("saisissez la liste de nombre séparée par une virgule : ")

print(nombres)

myList = nombres.split(",")

print(myList)
print (type(myList))

liste_entiers = []

somme = 0
nbr = 0
num = 0

for li in myList :
    nbr = int(li)
    liste_entiers.append(li)
    somme += nbr


moy = somme / len(liste_entiers)

print("la somme est ", somme)
print("la moy est ", moy)

for i in liste_entiers :
    if i > moy :
        num +=1

print("le nombre de nombres > à la moy est de ", num)