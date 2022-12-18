# Gale-Shapley-Algorithm
Introduction<br>
Dans la vie de tous les jours, on est confronté à prendre des décisions qui se présente sous forme de pairs de groupes, l’exemple le plus connu est celui du mariage stable où on a deux groupes, un groupe d’hommes et un autre de femme et qui cherchent à former des couples. Chaque membre des deux groupes possède un classement des membres du groupe opposé ordonné selon ses préférences pour son/sa partenaire idéal. L’objectif est que tout le monde s’associe avec une personne du groupe opposé et que cet arrangement soit « stable ». C’est à dire qu’il n’y a aucune situation où deux couples préféraient échanger de partenaire entre eux.<br><br>
L’algorithme de Gale-Shapley vient résoudre ce problème, et c’est ce qu’on va expliquer juste après.
Implémentation de l’algorithme de Gale-Shapley<br>
On a implémenté l’algorithme en Python.<br>
L'exemple choisie pour le déroulement de l’algorithme est le suivant :<br>
•	On est dans une section Master 2 IV<br>
•	La section a deux groupes (G1, G2)<br>
•	Chaque étudiant d'un groupe donné doit se mettre en binôme avec un étudiant de l'autre groupe<br>
•	Chaque étudiant a sa liste de préférence pour son prochain binôme<br>
•	Exemple g2_0= [3, 0, 1, 2] signifie que la liste de préférence de l’étudiant numéro 0 du Groupe 2 est comme suit : l’étudiant 3 du Groupe 1 puis l’étudiant 0 puis l’étudiant 1 puis l’étudiant 2<br>
•	Chaque étudiant du G2 sans binôme va choisir un étudiant du G1 par ordre de préférence<br>
•	Si l'étudiant g1 n'a pas encore un binôme donc il va accepter de se mettre en binôme<br>
•	Si l'étudiant g1 a déjà un binôme, donc il va choisir entre son binôme actuel et le nouvel étudiant en se basant sur sa liste de préférence<br>
•	Les numéros des étudiant du Groupe1 (g1_i) sont : 5, 6, 7, 8, 9<br>
•	Les numéros des étudiant du Groupe2 (g2_i) sont : 0, 1, 2, 3, 4<br>
