def NbrLigne (nomFic) :
	f = open (nomFic, "r")
	cpt=0
	for ligne in f :
		line = ligne.strip("\n")
		cpt+=1
	return cpt

# ~ print (NbrLigne("Demi.txt"))

# ~ f = open ("La_mesure_de_lhomme.txt","a")
# ~ f.write(" La mesure de l'homme. \n \n Ce n est pas celui qui critique qui est important, ni celui qui montre du doigt comment l homme fort trébuche ou comment l homme d action aurait pu faire mieux. \n L hommage est dû à celui ou à celle qui se bat dans l arène, dont le visage est couvert de poussière et de sueur, qui va de l avant vaillamment, qui commet deserreurs et en commettra encore, car il n y a pas d efforts humains sans erreurs et imperfections. C est à lui ou à elle qu appartient l hommage, à celui ou à celle dont l enthousiasme et la dévotion sont grands, à celui ou à celle qui se consume pour une cause importante, à celui ou à celle qui, au mieux, connaîtra le triomphe du succès, et au pis, s il échoue, saura qu il a échoué alors qu il risquait courageusement.")

f2 = open ("Demi.txt","r")
# ~ for ligne in f2 :
	# ~ f.write(ligne)

f = open ("La_mesure_de_lhomme.txt","r")
for line in f :
	print(line)
