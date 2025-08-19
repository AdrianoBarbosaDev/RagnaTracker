#Import models
from typing import List
from models.instancia import Instancia
from models.personagem import personagem
from database.buscas_db import buscarPersonagens, buscarInstancias

import os
import sys
import json

def startTracker():

    print("""
██████╗░░█████╗░░██████╗░███╗░░██╗░█████╗░████████╗██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░
██╔══██╗██╔══██╗██╔════╝░████╗░██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗
██████╔╝███████║██║░░██╗░██╔██╗██║███████║░░░██║░░░██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝
██╔══██╗██╔══██║██║░░╚██╗██║╚████║██╔══██║░░░██║░░░██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗
██║░░██║██║░░██║╚██████╔╝██║░╚███║██║░░██║░░░██║░░░██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝""")
    
    print ("1 - Personagens")
    print("2 - Instâncias")
    print("3- Sair")

    opcaoEscolhida = input("Escolha uma opção: ")

    if(int(opcaoEscolhida) == 1):
        print(buscarPersonagens())
    elif(int(opcaoEscolhida) == 2 ):
        print(buscarInstancias())
    else:
        print("Saindo..")


if __name__ == "__main__":
    print("rodando main.py")
    startTracker()