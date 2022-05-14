"""Description

La library chemin_minimale permet donner le chemin 
à prendre pour se rendre le plus vite posssible entre 
un départ et une arrivée sélectionnée.

Cette librairie fonctionne pour n'importe quelle taille de graphe.

Elle fonctionne pour n'importe quel chemin 
que ce soit un aller ou un retours. (de 1 à 16 et de 16 à 1).

Elle fonctionne également pour tous les points entre eux ou
pour tout les chemins envisageables même si le chemin minimal
nécessite une remonté dans le graphe.

Utilisez Le_plus_cours_chemin en entrant votre graphe, votre départ, votre arrivée 
et il vous sera retourné le chemin le plus cours ainsi que toutes ses étapes dans l'ordre.
"""



from .lib_donnee import Graphe
from .lib_temps import (_calcule_temps,_calcule_suivante)



def _ordre(graphe:Graphe)->str:
    """
Fonctionnalité:

Permet de déterminer si le chemin
effectué est un aller ou un retour 
(selon le sens du graphe)
-------------------------------
Exemple : 
---------
>>> _ordre('1','16')
'aller'

>>> _ordre('16','1')
'retour'
-------------------------------
"""
    sens = 0
    if int(graphe.depart) < int(graphe.arrivee):
        sens = 'aller'
    else: 
        sens = 'retour'
    return sens





def _temps_depuis_depart(graphe: Graphe) -> tuple[dict,float]:
    """

Fonctionnalité:

Permet de déterminer les chemins 
les plus cours entres le départ 
choisit et tout les points
-------------------------------
Exemple : 
---------
>>> temps_depuis_depart(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5),
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1","4")
    
{'1': 0.0, '2': 1.0, '3': 3.0, '4': 2.0}
-------------------------------
"""
    d0 = {sommet: float("inf") for sommet in graphe.sommets}
    d0[graphe.depart] = 0.0
    d1 = _calcule_suivante(graphe, d0)
    while d1 != d0:
        d0, d1 = d1, _calcule_suivante(graphe, d1)
    return d1





def _recuperation_candidat_min_chemin(graphe: Graphe) -> list[str, float]:
    """

Fonctionnalité:

Permet de récupérer l'étape finales (d1)
et ainsi connaître le temps entre le prédecesseur
et le sommet ou l'on se rends, détaillé en temps predecesseur et poids.
-------------------------------
Exemple : 
---------
_recuperation_candidat_min_chemin(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5),
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1","4")
    
['1', '2', 1.0, 1.0, '1', '3', 3.0, 5.0, '2', '1', 0.0, 1.0,
'2', '3', 3.0, 3.0, '2', '4', 2.0, 1.0, '3', '1', 0.0, 5.0,
'3', '2', 1.0, 3.0, '3', '4', 2.0, 1.0, '4', '2', 1.0, 1.0,
'4', '3', 3.0, 1.0]
-------------------------------
"""
    candidat = list()
    temps = _temps_depuis_depart(graphe,graphe.depart,graphe.arrivee)
    for sommet in graphe.sommets:
        for predecesseur,poids in graphe[sommet]:
            candidat.extend([sommet,predecesseur, temps[predecesseur], poids])
    return candidat





def _separate(graphe:Graphe)->list():
    """

Fonctionnalité:

Permet de regrouper dans une liste 
les différentes possibilitées de chemin 
pour un même sommet et la temps et poids  liées à ce chemin.

Ordonne la liste obtenue avant en list[list[]]
-------------------------------
Exemple : 
---------
>>> separate(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5),
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1","4")
    
[[['4', '2', 1.0, 1.0], ['4', '3', 3.0, 1.0]],
[['3', '1', 0.0, 5.0], ['3', '2', 1.0, 3.0], ['3', '4', 2.0, 1.0]],
[['2', '1', 0.0, 1.0], ['2', '3', 3.0, 3.0], ['2', '4', 2.0, 1.0]],
[['1', '2', 1.0, 1.0], ['1', '3', 3.0, 5.0]]]
-------------------------------
"""
    temps = _temps_depuis_depart(graphe)
    liste = _recuperation_candidat_min_chemin(graphe,temps)
    sens = _ordre(graphe)
    liste1 = list()
    liste_inter = list()
    liste_final = list()
    nb = 0
    j = 4
    for i in range(0,(len(liste)//4)):
        liste1.append(liste[nb:j])
        nb = nb+4
        j = j+4
    
    j = 1
    for i in range(0,len(liste1)-1):
        liste_inter.append(liste1[i])
        if (liste1[i])[0] == (liste1[j])[0]:
            j=j+1
        else:
            liste_final.append(liste_inter)
            liste_inter = list()
            j = j+1
    liste_inter.append(liste1[len(liste1)-1])
    liste_final.append(liste_inter)
    if sens == 'aller':
        liste_final= [num for num in reversed(liste_final)]
    return liste_final





def _trouve_chemin_minimal(graphe:Graphe)->list():
    """
    La fonction regarde chaque liste (par sommets)
    Elle additionne la temps[predecesseur] et le poids de l'arrête
    Puis elle récupère la liste parmis celle-ci dont cette somme est minimale (temps le cours)
    -------------------------------
    Exemple : 
    ---------
    >>> trouve_chemin_minimal(
        Graphe(sommets=["1", "2", "3", "4"],
        arretes=[("1", "2", 1),("2", "1", 1),
        ("1", "3", 5),("3", "1", 5),
        ("2", "3", 3),("3", "2", 3),
        ("2", "4", 1),("4", "2", 1),
        ("3", "4", 1),("4", "3", 1),]),
        "1","4")
        
    [['4', '2', 1.0, 1.0], ['3', '4', 2.0, 1.0],
    ['2', '1', 0.0, 1.0], ['1', '2', 1.0, 1.0]]
    -------------------------------
    """
    listes = _separate(graphe)
    newlist = list()
    liste_fi = list()
    for liste in listes:
        for candidat in liste:
            newlist.append(sum(candidat[-2:]))
        id=(newlist).index(min(newlist))
        newlist = list()
        mini = liste[id]
        liste_fi.append(mini)
    return liste_fi





def _organisation_ordre(graphe:Graphe)->list():
    """

Fonctionnalité:

Step1 : 

Cherche dans l'ordre de 
la liste vu auparavant la liste 
dont le sommet commence par l'arrivée 
et le met dans une nouvelle liste nommée recup
Puis 
Récupère dans une liste nommée num le 
numéro du predecesseur et  le numéro du sommet
Puis
Supprime cette liste dans la liste all

Step2:

On parcours all et si le predeceur de la 
liste de départ enregistré dans num 
est égale au sommet de la liste parcourue,
alors c'est le bon chemin minimal, 
une connection est effectuée.

Alors on récupère le chemin qui match 
avec celui enregistré avant et on 
le supprime de la liste all

Step3:

Réitération de ce processus pour obtenir le chemin minimal
Puis
Inverse la liste pour la suite pour que l'on est la liste dans le sens du départ à l'arrivée
-------------------------------
Exemple : 
---------
>>> organisation_ordre(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5),
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1","4")
    
[['2', '1', 0.0, 1.0], ['4', '2', 1.0, 1.0]]
-------------------------------
"""
    all = _trouve_chemin_minimal(graphe)
    
    recup = list()
    k = 0
    num = list()
        
    for i in range(0,len(all)-1):
        if (all[k])[0] == graphe.arrivee :
            recup.append(all[k])
            num.append((all[k])[1])
            num.append((all[k])[0])
            del all[k]
            k = k + 1
        else : 
            k = k + 1
    
    for i in all:
        for j in all:
            if j[0] == num[0] and j[1] != num[1]:
                num = list()
                recup.append(j)
                num.append(j[1])
                num.append(j[0])
                del j
                
    recup= [num for num in reversed(recup)]
    if (recup[0])[0] == graphe.depart:
        del (recup[0])              
    return recup 




def Le_plus_cours_chemin(graphe: Graphe):
    """

Fonctionnalité:

Permet d'afficher le résultat sous 
la forme de phrase en détaillant 
le chemin sommet par sommet et le 
temps pris pour chaque arretes 
entre sommets.
Puis
Détaille le départ-arrivée-Temps 
de trajet total
-------------------------------
Exemple : 
---------
>>> Le_plus_cours_chemin(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5), 
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1","4")

Dirigez-vous de 1 vers 2, le temps pour s'y rendre sera de 1.0 minutes
Dirigez-vous de 2 vers 4, le temps pour s'y rendre sera de 1.0 minutes
Le temps total pour se rendre de 1 à 4 est de 2.0 minutes
-------------------------------
"""
    chemin = _organisation_ordre(graphe)
    resultat = _calcule_temps(graphe)
    for i in chemin:
        print(f"Dirigez-vous de {i[1]} vers {i[0]}, le temps pour s'y rendre sera de {i[3]} minutes")
    print(f"Le temps total pour se rendre de {graphe.depart} à {graphe.arrivee} est de {resultat} minutes")