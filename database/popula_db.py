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
    #Populando
    cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lenahri', 'Arcebispa')")
    cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lunahri', 'Bioquimica')")
    conexao.commit()


    
    instancias = [
        ("Vila dos Porings",24,1,"SOLO OU GRUPO"),
        ("Torre sem Fim",168,5,"SOLO OU GRUPO"),
        ("Batalha dos Orcs",24,1,"SOLO OU GRUPO"),
        ("Ninho de Nidhogg",24,1,"SOLO OU GRUPO"),
        ("Altar do Selo",12,1,"SOLO OU GRUPO"),
        ("Torneio de Magia",24,2,"SOLO"),

        ("Memórias de Sarah",24,2,"SOLO OU GRUPO"),
        ("Laboratório Werner",24,2,"SOLO OU GRUPO"),
        ("Base Militar",24,2,"SOLO OU GRUPO"),
        ("Salão de Ymir",24,2,"SOLO OU GRUPO"),
        ("Infinite Space",24,3,"SOLO OU GRUPO"),

        ("Palácio das Mágoas",24,2,"SOLO OU GRUPO"),
        ("Pesadelo Musical",24,2,"SOLO OU GRUPO"),
        ("Airship Assault",24,2,"SOLO OU GRUPO"),
        ("Torre do Demônio",24,3,"SOLO OU GRUPO"),
        ("17.2 Water Garden",24,3,"SOLO OU GRUPO"),
        ("17.2 Flower Garden",24,3,"SOLO OU GRUPO"),

        ("Maldição de Glast Heim [NORMAL]",24,5,"SOLO OU GRUPO"),
        ("Maldição de Glast Heim [HARD]",24,10,"SOLO OU GRUPO"),
        ("Fall of Glast Heim",24,2,"SOLO OU GRUPO"),
        ("Charlestom em Crise",24,2,"SOLO OU GRUPO"),
        ("Hey! Sweety!",24,3,"SOLO OU GRUPO"),
        ("Lost in Time",24,3,"SOLO OU GRUPO"),
        ("Caverna de Buwaya",24,3,"SOLO OU GRUPO"),

        ("Fábrica de Brinquedos",24,3,"SOLO OU GRUPO"),
        ("Lago de Bakonawa",24,2,"SOLO OU GRUPO"),
        ("Laboratório Central",24,2,"SOLO OU GRUPO"),
        ("Sarah vs Fenrir",24,2,"SOLO OU GRUPO"),
        ("Susurro Sombrio",24,2,"SOLO OU GRUPO"),
        ("Labotarório de Wolfchev",24,2,"SOLO OU GRUPO"),
        ("Templo do Demonio Rei",24,5,"SOLO OU GRUPO"),

        ("Sanctuary Purification",24,5,"SOLO OU GRUPO"),
        ("Fall of Glast Heim [HARD]",24,4,"SOLO OU GRUPO"),
        ("EDDA Bioresearch Laboratory",24,5,"SOLO OU GRUPO"),
        ("Old Glast Heim [CHALLENGE]",24,20,"SOLO OU GRUPO"),
        ("Villa of Deception",24,3,"SOLO OU GRUPO"),
        ("Villa of Zeny",24,3,"DUPLA"),
    ]

    cur.executemany("INSERT INTO instancia (nome,recarga,moedas,categoria)VALUES(?,?,?,?)",instancias)
    # cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lenahri', 'Arcebispa')")
    # cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lunahri', 'Bioquimica')")
    conexao.commit()
