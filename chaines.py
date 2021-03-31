def searchC (mot,chaine) :
	trouve = chaine.find(mot)
	if trouve == -1 :
		return False
	else :
		return trouve

# ~ print (searchC("bla","dabladou"))

chaine = "La v13 3st un myst3r3 qu'1l faut v1vr3, et non un probl3m3 a r3soudr3.Gandh1"
nouvelleChaine=""
for i in range (len(chaine)):
	if chaine[i] == "1" :
		nouvelleChaine+="i"
	elif chaine[i] == "3" :
		nouvelleChaine+="e"
	else :
		nouvelleChaine+=chaine[i]

# ~ print (nouvelleChaine)

def compteur (l,c) :
	cpt = 0
	for i in range (len(c)) :
		if l == c[i] :
			cpt+=1
	return cpt

# ~ print (compteur ("i","sbdfizurozjfbkzi"))

def inverse (c) :
	new_c = c[::-1]
	return new_c
	

# ~ print(inverse("mot"))
