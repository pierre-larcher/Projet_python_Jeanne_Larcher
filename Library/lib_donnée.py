"""Description.
Classe Permettant de représenter les données d'un problème.
"""

from dataclasses import dataclass
from serde import serde
from typing import Any, Union, Iterator


@serde                  
class Graphe:
        
        sommets: list[str]
        arretes: list[tuple[str, str, float]] = [
            (depart, arrivee, float(poids)) for depart, arrivee, poids in arretes]
        
        def sommets(self) -> Iterator[str]:
            return iter(self.sommets)
        
        def arretes(self) -> Iterator[str]:
            return iter(self.arretes)