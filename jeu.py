# -*- encoding utf8 -*-

import random

tableau_jeu=[]

for i in range (0,10) :
	tableau_jeu.append(random.randint(0,10))

# ~ nombre = int(input("Mettez un nombre : "))
# ~ trouve = False
# ~ for j in range (0,len(tableau_jeu)):
	# ~ if nombre == tableau_jeu[j] :
		# ~ trouve = True
		# ~ break
# ~ if trouve :
	# ~ print ("Gagné !")
# ~ else :
	# ~ print ("Perdu")

tableau_jeu.sort()
print(tableau_jeu)
nombre = int(input("Mettez un nombre : "))
trouve = False
for j in range (0, len(tableau_jeu)) :
	print (tableau_jeu[j])
	if nombre < tableau_jeu[j] :
		break
	if nombre == tableau_jeu[j] :
		trouve = True
		break
if trouve :
	print ("Gagné !")
else :
	print ("Perdu")
