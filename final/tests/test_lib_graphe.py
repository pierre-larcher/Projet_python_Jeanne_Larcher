"""Description
Tests automatiques de la classe Graphe.
Le but ici est de penser à toute éventualité d'erreur qui mènerai à faire planter la librairie.
Nous nous assurons que la classe Graphe se crée bien.
"""

"""Description.
Tests automatiques de lib_graphe.
"""
import pytest
from final.lib_donnee import (
    Graphe)


def test_init():
    exemple = Graphe(
        sommets=["1", "2", "3"], arretes=[("1", "2", 1.5), ("1", "3", 1.0)]
    )
    assert isinstance(exemple, Graphe)


def test_repr():
    exemple = Graphe(sommets=["1", "2", "3"], arretes=[("1", "2", 1), ("1", "3", 1.5)])
    attendu = (
        "Graphe(sommets=['1', '2', '3'], arretes=[('1', '2', 1.0), ('1', '3', 1.5)])"
    )
    assert repr(exemple) == attendu


def test_egalite_naive():
    exemple1 = Graphe(sommets=["1", "2", "3"], arretes=[("1", "2", 1.5), ("1", "3", 1)])
    exemple2 = Graphe(sommets=["1", "2", "3"], arretes=[("1", "2", 1.5), ("1", "3", 1.0)]
    )
    assert exemple1 == exemple2


def test_egalite():
    exemple1 = Graphe(
        sommets=["1", "2", "3"], arretes=[("1", "2", 1.5), ("1", "3", 0.5)]
    )
    exemple2 = Graphe(
        sommets=["1", "3", "2"], arretes=[("1", "3", 0.5), ("1", "2", 1.5)]
    )
    assert exemple1 == exemple2


def test_inegalite():
    exemple1 = Graphe(
        sommets=["1", "2", "3"], arretes=[("1", "2", 1.5), ("1", "3", 0.5)]
    )
    exemple2 = Graphe(
        sommets=["1", "3", "2"], arretes=[("1", "3", 0.5), ("1", "2", 1.0)]
    )
    assert exemple1 != exemple2




