animaux = ["lapin","chat","chien","chiot","dragon","ornithorynque"]

#afficher la liste
print (animaux)

#liste inversée
animaux.reverse()
print (animaux)

#trier la liste
animaux.sort()
print (animaux)

#ajouter troll
animaux.append("troll")
#supprimer les animaux domestiques
for animal_domestique in ("lapin","chat","chien","chiot") :
	animaux.remove(animal_domestique)
print (animaux)
