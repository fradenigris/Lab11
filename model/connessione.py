from dataclasses import dataclass, field
from datetime import time

@dataclass
class Connessione:
    id: int
    id_rifugio1: int
    id_rifugio2: int
    distanza: int
    difficolta: str
    durata: time
    anno: int
    id_rifugi: set = field(default_factory=set)


    def __eq__(self, other):
        return isinstance(other, Connessione) and self.id == other.id

    def __str__(self):
        return (f"Sentiero tra i rifugi con i seguenti ID: {self.id_rifugio1} - {self.id_rifugio2}. Distanza: {self.distanza} km. "
                f"Difficolta': {self.difficolta}, durata: {self.durata}")

    def __repr__(self):
        return (f"Sentiero tra i rifugi con i seguenti ID: {self.id_rifugio1} - {self.id_rifugio2}. Distanza: {self.distanza} km. "
                f"Difficolta': {self.difficolta}, durata: {self.durata}")

    def __hash__(self):
        return hash(self.id)