#-*- encoding utf8 -*-

import random

cagnotte = 500
gains = 0
continuer = "o"
while cagnotte > 0 and continuer == "o":
	numeroGagnant = random.randint(0,49)
	# ~ print (numeroGagnant)
	numeroChoisi = int(input("Choisissez un numéro : "))
	sommeMise = int(input("Quelles sera la somme misée ? "))
	while sommeMise > cagnotte :
		print ("Vous ne pouvez pas mettre plus d'argent que ce que vous possedez")
		sommeMise = int(input("Quelles sera la somme misée ? "))
	cagnotte -= sommeMise
	#le cas de la victoire absolue
	if numeroChoisi == numeroGagnant :
		print ("Incroyable ! Vous avez gagné !")
		gains = sommeMise*3
		cagnotte = cagnotte+sommeMise+gains
		print ("Vous avez gagné",str(gains),"euros.\nVotre cagnotte est à",str(cagnotte),"euros actuellement.")
		continuer = input("Voulez-vous continuer ? [o/n] ")
	#le cas de la même couleur
	elif ((numeroChoisi % 2 == 0) and (numeroGagnant % 2 == 0)) or ((numeroChoisi % 2 == 1) and (numeroGagnant % 2 == 1)):
		print ("Le numéro misé est de la même couleur que le numéro gagnant !")
		gains = sommeMise*0.5
		cagnotte = cagnotte+sommeMise+gains
		print ("Vous avez gagné",str(gains),"euros.\nVotre cagnotte est à",str(cagnotte),"euros actuellement.")
		continuer = input("Voulez-vous continuer ? [o/n] ")
		#perte
	else :
		print ("Vous avez perdu...")
		print ("Vous avez perdu",str(sommeMise),"euros.\nVotre cagnotte est à",str(cagnotte),"euros actuellement.")
		if cagnotte == 0 :
			break
		continuer = input("Voulez-vous continuer ? [o/n] ")
if cagnotte == 0 :
	print ("Vous n'avez plus d'argent... Revenez le mois prochain après le salaire !")
if continuer == "n" :
	print ("Vpus partez avec",str(cagnotte),"euros.\nMerci pour votre visite ! À bientôt !")
