def salaire_mensuel(salaire_annuel) :
    salaireMensuel = salaire_annuel / 12
    return (salaireMensuel)

def salaire_hebdomadaire(salaire_mensuel) :
    salaireHebdo = salaire_mensuel / 4
    return (salaireHebdo)

def salaire_horaire(salaire_hebdomadaire, heures_travaillees) :
    salaireHor = salaire_hebdomadaire / heures_travaillees
    return (salaireHor)


salaireAnn = float(input("Quel est votre salaire annuel ? "))
HeureSemaine = float(input("Combien d'heure par semaine travaillez vous ? "))

if HeureSemaine == 0 :
    raise SystemExit("Nombre d'heure = 0 impossible de faire les caluls")
else :
    sal = salaire_mensuel(salaireAnn)
    hebdo = salaire_hebdomadaire(sal)
    salHora = salaire_horaire(hebdo, HeureSemaine)

print(f"Votre salaire horaire est de {salHora} euros")
