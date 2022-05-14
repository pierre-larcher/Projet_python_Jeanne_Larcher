"""Description
Librairie représentant un objet graphe
"""
from typing import Any, Union


class Graphe:
    def __init__(
        
        self,
        sommets: list[str],
        arretes: list[tuple[str, str, Union[int, float]]]
    ):
        """
        It takes a list of vertices and a list of edges, and returns a graph
        
        :param sommets: list[str]
        :type sommets: list[str]
        :param arretes: list[tuple[str, str, Union[int, float]]]
        :type arretes: list[tuple[str, str, Union[int, float]]]
        """
        self._sommets = sommets
        self._arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(poids)) for depart, arrivee, poids in arretes
        ]

    def __repr__(self) -> str:
        return f"Graphe(sommets={repr(self._sommets)}, arretes={repr(self._arretes)})"

    def __eq__(self, autre: Any) -> bool:
        if type(autre) != type(self):
            return False
        if sorted(self._sommets) != sorted(autre._sommets):
            return False
        if sorted(self._arretes) != sorted(autre._arretes):
            return False
        return True

    def __iter__(self):
        return iter(self._arretes)
    
    def sommets(self):
        return iter(self._sommets)
    
    def arretes(self):
        return iter(self._arretes)
    
    def __getitem__(self, arrivee: str):
        for gauche, droite, poids in self._arretes:
            if droite == arrivee:
                yield gauche, poids


