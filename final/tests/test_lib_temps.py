"""Description.
Tests automatiques de lib_temps.
"""
import pytest
from final.lib_donnee import Graphe
from final.lib_temps import (_calcule_suivante, _calcule_temps )

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

def test_calcule_suivante(graphe):
    d0 = {"1": 0.0, "2": float("inf"), "3": float("inf"), "4": float("inf")}
    d1 = {"1": 0.0, "2": 1.0, "3": 5.0, "4": float("inf")}
    d2 = {"1": 0.0, "2": 1.0, "3": 4.0, "4": 2.0}
    d3 = {"1": 0.0, "2": 1.0, "3": 3.0, "4": 2.0}
    d4 = {"1": 0.0, "2": 1.0, "3": 3.0, "4": 2.0}
    assert _calcule_suivante(graphe, "1", d0) == d1
    assert _calcule_suivante(graphe, "1", d1) == d2
    assert _calcule_suivante(graphe, "1", d2) == d3
    assert _calcule_suivante(graphe, "1", d3) == d4
    
def test_calcule_temps(graphe):
    assert _calcule_temps(graphe, "1", "3") == 3.0
    
   