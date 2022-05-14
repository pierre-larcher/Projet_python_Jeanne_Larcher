"""Description
Le test_lib_chemin permet de vérifier que la librairie chemin_minimal fonctionne parfaitement.
Le but ici est de penser à toute éventualité d'erreur qui mènerai à faire planter la librairie.
"""

import pytest

from lib_graphe import Graphe

from lib_chemin_minimal import (_ordre,_temps_depuis_depart,
                                _recuperation_candidat_min_chemin,
                                _separate,
                                _trouve_chemin_minimal,
                                _organisation_ordre)

@pytest.fixture
def graphe():
    return Graphe(
        sommets=["1", "2", "3", "4"],
        arretes=[
            ("1", "2", 1),
            ("2", "1", 1),
            ("1", "3", 5),
            ("3", "1", 5), 
            ("2", "3", 3),
            ("3", "2", 3),
            ("2", "4", 1),
            ("4", "2", 1),
            ("3", "4", 1),
            ("4", "3", 1),
        ]
    )
    
def test_odre_aller():
    exemple = _ordre("1","4")
    attendu = "aller"
    assert exemple == attendu
    
def test_odre_retour():
    exemple = _ordre("4","1")
    attendu = "retour"
    assert exemple == attendu
    
    
        
def  test_temps_depuis_depart(graphe):
    exemple = _temps_depuis_depart(graphe,"1","4")
    attendu = {'1': 0.0, '2': 1.0, '3': 3.0, '4': 2.0}
    assert exemple==attendu
    
def test_recuperation_candidat_min_chemin(graphe):
    exemple = _recuperation_candidat_min_chemin(graphe,"1","4")
    attendu = ['1', '2', 1.0, 1.0,
               '1', '3', 3.0, 5.0, 
               '2', '1', 0.0, 1.0,
               '2', '3', 3.0, 3.0,
               '2', '4', 2.0, 1.0,
               '3', '1', 0.0, 5.0,
               '3', '2', 1.0, 3.0,
               '3', '4', 2.0, 1.0,
               '4', '2', 1.0, 1.0,
               '4', '3', 3.0, 1.0]
    assert exemple == attendu
 
def test_separate(graphe):
    exemple = _separate(graphe,"1","4")
    attendu = [[['4', '2', 1.0, 1.0],
                ['4', '3', 3.0, 1.0]],
                [['3', '1', 0.0, 5.0],
                ['3', '2', 1.0, 3.0],
                ['3', '4', 2.0, 1.0]],
                [['2', '1', 0.0, 1.0],
                ['2', '3', 3.0, 3.0],
                ['2', '4', 2.0, 1.0]],
                [['1', '2', 1.0, 1.0],
                ['1', '3', 3.0, 5.0]]]
    assert exemple == attendu
    
def test_trouve_chemin_minimal(graphe):
    exemple = _trouve_chemin_minimal(graphe, "1","4")
    attendu = [['4', '2', 1.0, 1.0],
               ['3', '4', 2.0, 1.0],
               ['2', '1', 0.0, 1.0],
               ['1', '2', 1.0, 1.0]]
    assert exemple == attendu
    
def test_organisation_ordre(graphe):
    exemple = _organisation_ordre(graphe,"1","4") 
    attendu = [['2', '1', 0.0, 1.0],
               ['4', '2', 1.0, 1.0]]
    assert exemple == attendu
    


