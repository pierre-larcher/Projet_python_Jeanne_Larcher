"""Description.
Classe Permettant de représenter les données d'un problème.
"""

from serde import serde
from dataclasses import dataclass
from typing import Any, Union

@dataclass(eq=False)
@serde                  
class Graphe:
        
        sommets: list[str]
        arretes: list[tuple[str, str, float]]
        depart: str
        arrivee: str
        