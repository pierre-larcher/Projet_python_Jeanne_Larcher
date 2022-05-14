from lib_graphe import Graphe


def _calcule_suivante(graphe: Graphe, depart: str, temps: dict[str, float]) -> dict[str, float]:
    """

Fonctionnalité:

Permet de retourner un dictionnaire 
qui associe pour chaque sommet la distance 
entre le point de départ et le sommet associé.
Elle permet en fait d'executer une étape de calcul
de la même manière que nous le faisions en cours
-------------------------------
Exemple : 
---------
>>> _calcule_suivante(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5), 
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1",
    {"1": 0.0, "2": float("inf"), "3": float("inf"), "4": float("inf")})
    
{'1': 0.0, '2': 1.0, '3': 5.0, '4': inf}
-------------------------------
"""
    resultat = dict()
    for sommet in graphe.sommets():
        resultat[sommet] = min(
            poids + temps[predecesseur] for predecesseur, poids in graphe[sommet]
        )
    resultat[depart] = 0.0
    return resultat


def _calcule_temps(graphe: Graphe, depart: str, arrivee: str) -> float:
    """

Fonctionnalité:

Utilise la fonction _calcule_suivante en réitération jusqu'à ce que l'input soit égale à l'output, 
Cela signifie que le min pour chaque sommets et le point de départ à été trouvé.
-------------------------------
Exemple : 
---------
>>> calcule_temps(
    Graphe(sommets=["1", "2", "3", "4"],
    arretes=[("1", "2", 1),("2", "1", 1),
    ("1", "3", 5),("3", "1", 5),
    ("2", "3", 3),("3", "2", 3),
    ("2", "4", 1),("4", "2", 1),
    ("3", "4", 1),("4", "3", 1),]),
    "1","4")
    
2.0
-------------------------------
"""
    d0 = {sommet: float("inf") for sommet in graphe.sommets()}
    d0[depart] = 0.0
    d1 = _calcule_suivante(graphe, depart, d0)
    while d1 != d0:
        d0, d1 = d1, _calcule_suivante(graphe, depart, d1)
    return d1[arrivee]