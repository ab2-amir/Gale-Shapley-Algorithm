# Gale-Shapley-Algorithm
## Introduction<br>
Dans la vie de tous les jours, on est confronté à prendre des décisions qui se présente sous forme de pairs de groupes, l’exemple le plus connu est celui du mariage stable où on a deux groupes, un groupe d’hommes et un autre de femmes et qui cherchent à former des couples. Chaque membre des deux groupes possède un classement des membres du groupe opposé ordonné selon ses préférences pour son/sa partenaire idéal. L’objectif est que tout le monde s’associe avec une personne du groupe opposé et que cet arrangement soit « stable ». C’est à dire qu’il n’y a aucune situation où deux couples préféraient échanger de partenaire entre eux.<br>
L’algorithme de Gale-Shapley vient résoudre ce problème, et c’est ce qu’on va expliquer juste après.<br><br>
## Implémentation de l’algorithme de Gale-Shapley<br>
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

## Explication du code<br>
### La fonction g1PrefersCurrent_g2Overg2()<br>
La fonction permet de vérifier si l’étudiant du groupe 1 préfère son binôme actuel au nouvel étudiant qui veut se mettre en binôme avec lui, si c’est le cas la fonction renvoie vrai si non faux <br><br>
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/fct_prefer.png">
 <img alt="YOUR-ALT-TEXT" src="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/fct_prefer.png">
</picture><br>

### La fonction stableBinome()<br>
La fonction génère des binômes avec un arrangement stable de tel sorte qu’il n’y a pas de situation où deux binômes préfère échanger entre eux.
Si on traduit la fonction en pseudo code :<br><br>
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/pseudo-code.png">
 <img alt="YOUR-ALT-TEXT" src="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/pseudo-code.png">
</picture><br>

### Main de l’algorithme<br>
On a créé une matrice qui contient les listes de préférence de 10 étudiants, les 5 premier étudiant sont du groupe 2 et les 5 dernier sont du groupe 1<br><br>
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/main.png">
 <img alt="YOUR-ALT-TEXT" src="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/main.png">
</picture><br>

### Affichage<br>
En résultat final de l’algorithme on a eu les binômes stables avec la préférence de chaque étudiant<br><br>
<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/result.png">
 <img alt="YOUR-ALT-TEXT" src="https://github.com/abdou-amir/Gale-Shapley-Algorithm/blob/main/ressources/result.png">
</picture><br>

Cela signifie que l’étudiant g1_5 est en binôme avec l’étudiant g2_1, sachant que g2_1 est le troisième choix de g1_5 et que g1_5 est le premier choix de g2_1<br>
De même pour le reste des binômes.<br>

