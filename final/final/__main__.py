"""Description.
Application ligne de commande pour la librairie.
"""

from .lib_donnee import Graphe
from .lib_temps import _calcule_temps,_calcule_suivante
from .lib_chemin_minimal import Le_plus_cours_chemin
from serde.json import from_json, to_json
import typer
from rich import print

application = typer.Typer()

@application.command()
def exemple(nom_fichier: str):
    exemple = Graphe(
        sommets=["1", "2", "3", "4","5","6","7","8","9","10","11","12","13","14","15","16"],
        arretes=[
            ("1", "2", 5),
            ("2", "1", 5),
            ("1", "3", 9),
            ("3", "1", 9),
            ("1", "4", 4),
            ("4", "1", 4),
            ("2", "5", 3),
            ("5", "2", 3), 
            ("2", "6", 2),
            ("6", "2", 2),
            ("3", "4", 4),
            ("4", "3", 4),
            ("3", "6", 1),
            ("6", "3", 1),
            ("4", "7", 7),
            ("7", "4", 7),
            ("5", "8", 4),
            ("8", "5", 4),
            ("5", "9", 2),
            ("9", "5", 2),
            ("5", "10", 9),
            ("10", "5", 9),
            ("6", "7", 3),
            ("7", "6", 3),
            ("6", "10", 9),
            ("10", "6", 9),
            ("6", "11", 6),
            ("11", "6", 6), 
            ("7", "11", 8),
            ("11", "7", 8),
            ("7", "15", 5),
            ("15", "7", 5),
            ("8", "12", 5),
            ("12", "8", 5),
            ("9", "8", 3),
            ("8", "9", 3),
            ("9", "13", 10),
            ("13", "9", 10),
            ("10", "9", 6),
            ("9", "10", 6),
            ("10", "13", 5),
            ("13", "10", 5),
            ("10", "14", 1),
            ("14", "10", 1),
            ("11", "14", 2),
            ("14", "11", 2),
            ("12", "16", 9),
            ("16", "12", 9), 
            ("13", "12", 4),
            ("12", "13", 4),
            ("13", "14", 3),
            ("14", "13", 3),
            ("14", "16", 4),
            ("16", "14", 4),
            ("15", "14", 4),
            ("14", "15", 4),
            ("15", "16", 3),
            ("16", "15", 3),
        ],
        depart = "1",
        arrivee = "16"
    )

    code = to_json(exemple)

    with open(nom_fichier, "w") as fichier:
        fichier.write(code)
        
@application.command()
def calcule(nom_fichier: str):
    with open(nom_fichier, "r") as fichier:
        code = fichier.read()
        
    donnees = from_json(Graphe, code)
    solution = Le_plus_cours_chemin(donnees)
    print(solution)
     
        
        
if __name__ == "__main__":
    application()