
from typing import List
from models.instancia import Instancia
from models.personagem import personagem, personagens

import os
import sys
import json

CAMINHO_JSON = "data/dados.json"
def carregar_clientes(caminho=CAMINHO_JSON) -> List[Instancia]:
    if not os.path.exists(caminho):
        print("Nãoi achei")
        return []
    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)
        return [Instancia.from_dict(item) for item in dados]
    print(dados)