# Gale–Shapley algorithm 

#PSEUDO CODE:

# Initialise tous les étudiants du groupe 1 et groupe 2 a étudiant sans binome
# Tq il existe un étudiant g2 sans binome
# {
	# récuperer l'étudiant g1 le plus préferer dans la liste de g2
	# g1 = g2_preference_liste 

	# if (g1 est sans binome)
	#		(g1, g2) deviennent binome
	# else
	# 		si (g1 préfere le nouvel étudiant g2 a g2')
	# 			(g1, g2) alors il deviennent binome
	# 			 g2' l'encien binome de g1 deviens sans binome
	# 		else
	# 			(g1, g2') rester ensemble
# }        
	

# L'exemple choisie pour le déroulement de l’algorithme est le suivant :
# •	On est dans une section Master 2 IV
# •	La section a deux groupes (G1, G2)
# •	Chaque étudiant d'un groupe donné doit se mettre en binôme avec un étudiant de l'autre groupe
# •	Chaque étudiant a sa liste de préférence pour son prochain binôme
# •	Exemple g2_0= [3, 0, 1, 2] signifie que la liste de préférence de l’étudiant numéro 0 du Groupe 2 est comme suit : l’étudiant 3 du Groupe 1 puis l’étudiant 0 puis l’étudiant 1 puis l’étudiant 2
# •	Chaque étudiant du G2 sans binôme va choisir un étudiant du G1 par ordre de préférence
# •	Si l'étudiant g1 n'a pas encore un binôme donc il va accepter de se mettre en binôme
# •	Si l'étudiant g1 a déjà un binôme, donc il va choisir entre son binôme actuel et le nouvel étudiant en se basant sur sa liste de préférence
# •	Les numéros des étudiant du Groupe1 (g1_i) sont : 5, 6, 7, 8, 9
# •	Les numéros des étudiant du Groupe2 (g2_i) sont : 0, 1, 2, 3, 4

 
# N est le Nombre d'étudiants en Groupe 1 (G1) et en Groupe 2 (G2)
N = 5

# Fonction qui return True si 
# l'étudiant g1 du Groupe 1 prfère son binome actuelle current_g2 
# par rapport à g2 (le nouveau choix)
# Dans le cas contraire la fonction return False
def g1PrefersCurrent_g2Overg2(prefer, g1, g2, current_g2):

    # verifier si g1 préfere g2 a son binome actuel (current_g2)
	for i in range(N):

        # si current_g2 est préfré a g2 
        # dans la liste de preference
        # alors g1 reste avec son binome actuel (current_g2)
		
		if (prefer[g1][i] == current_g2):
			return True

        # si g1 prefére g2 a son binome actuel (current_g2)
        # alors g1 change de binome avec g2

		if (prefer[g1][i] == g2):
			return False

# fonction qui return une liste de l'indice de préfrence 
# des étudiants g1 avec leurs binome g2
# (3, 1) signifie que g2 est le 3eme choix de g1 
# et que g1 et le 1er choix de g2
def rankG1(prefer, g1Partner, N):
	list_rank = []
	k = 0
	for i in range(N):
		j = 0
		found = False
		while(j < N and not found):
			if(g1Partner[k] == prefer[N + i][j]):
				list_rank.append(j+1)
				found = True
			j += 1
		k += 1
	return list_rank


# Les étudiants g2 du Groupe2 sont énumeré de 0 à N (0-4)
# Les étudiants g1 du Groupe1 sont énumeré de N à 2N-1 (5-9)
def stableBinome(prefer):

	#liste qui contient la préference de l'étudiant g2 a son binome g1
	rank = []

    # g1Partner[i] contient le numéro de l'étudiant g2 en binome avec l'étudiant g1 numéro N+i 
    # Si g1partner[i] = -1 alors g1 est sans binome

    # On initialise g1partner a -1 (tous les étudiants g1 sans binome)
	g1Partner = [-1 for i in range(N)]

    # mFree[i] contient l'état de l'étudiant g2
    # True: n'a pas de binome
    # False: a un binome

    # On initialise tous les étudiants g2 au statut (sans binome)
	mFree = [True for i in range(N)]

    # Le nombre d'étudiant g2 sans binome
	freeCount = N

    #Tq il y'a un étudiant g2 sans binome
	while (freeCount > 0):
		
		# On prend le premier étudiant g2 sans binome
		g2 = 0
		while (g2 < N):
			if (mFree[g2] == True):
				break
			g2 += 1

        # On parcours la liste de préference de g2 sans binome
		i = 0
		while (i < N and mFree[g2] == True):

            # On prend g1 l'étudiant préferer de g2
			g1 = prefer[g2][i]

            # Si g1 de la liste de préference de g2 est sans binome 
            # alors les deux étduiant se mettent en binome
			if (g1Partner[g1 - N] == -1):
				g1Partner[g1 - N] = g2 # assigner le binome (g1, g2)
				mFree[g2] = False # g2 deviens avec binome
				freeCount -= 1 #le nombre d'étudiant g2 sans binome réduit de 1
				rank.append(i+1) #save l'indice de préferencev(1er, 2eme, 3eme etc..)


			else:

                # Si g1 a deja un binome
                # On récupère son binome actuel (current_g2)
				current_g2 = g1Partner[g1 - N]

                # Si g1 prefere le nouvel étudiant a son binome actuel 
				if (g1PrefersCurrent_g2Overg2(prefer, g1, g2, current_g2) == False):
					g1Partner[g1 - N] = g2 # assigner le binome (g1, g2)
					mFree[g2] = False # g2 deviens avec binome
					mFree[current_g2] = True # l'étudiant actuel (current_g2) deviens sans binome

			i += 1

	# Affichage
	print("g1 ", " \tg2", "\tpréference")
	rankg1 = rankG1(prefer, g1Partner, N)

	for i in range(N):
		print(i + N, "\t", g1Partner[i], "\t(", rankg1[i], ",", rank[i], ")")





# Les étudiant du Groupe1 (g1) sont: 5, 6, 7, 8, 9
# Les étudiant du Groupe2 (g2) sont: 0, 1, 2, 3, 4

# Liste de préference
prefer = [[6, 5, 7, 8, 9], #liste de préference de g2_0
        [5, 6, 8, 9, 7], #liste de préference de g2_1
		[8, 9, 5, 6, 7], #liste de préference de g2_2
        [8, 9, 7, 6, 5], #liste de préference de g2_3
        [5, 7, 6, 8, 9], #liste de préference de g2_4

        [3, 2, 1, 0, 4], #liste de préference de g1_5
		[1, 3, 0, 2, 4], #liste de préference de g1_6
        [0, 1, 2, 3, 4], #liste de préference de g1_7
		[1, 0, 2, 3, 4], #liste de préference de g1_8
        [0, 3, 2, 1, 4]] #liste de préference de g1_9

stableBinome(prefer)



