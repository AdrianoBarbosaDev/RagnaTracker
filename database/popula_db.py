import sqlite3
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from conexao import conectar
from dotenv import load_dotenv
# from utils.InstanciaCategoriaEnum import Categoria;

conexao = conectar()

if conexao:
    # Cria Cursor que ira popular as tabelas
    cur = conexao.cursor()

    #Populando tabela de instâncias
    instancias = [
        ("Altar do Selo",24,1,"SOLO OU GRUPO"),
        ("Infinite Space",24,0,"SOLO OU GRUPO"),
        ("Torre sem Fim",24,0,"SOLO OU GRUPO"),
        ("Ninho de Nidhogg",24,1,"SOLO OU GRUPO"),
    ]
    cur.executemany("INSERT INTO instancia (nome,recarga,moedas,categoria)VALUES(?,?,?,?)",instancias)
    # cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lenahri', 'Arcebispa')")
    # cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lunahri', 'Bioquimica')")
    conexao.commit()
