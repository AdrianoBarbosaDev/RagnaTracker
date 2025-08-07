from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Instancia:
    id: str = ''
    nome: str = ''
    recarga: str = ''
    moedas: int = 0
    categoria: str = '' #Solo ou grupo
    tempoEstimado: int = 0

    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        return Instancia(**data)