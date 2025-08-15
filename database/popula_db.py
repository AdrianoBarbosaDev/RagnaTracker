import sqlite3
import os
from dotenv import load_dotenv
from conexao import conectar
# from utils.InstanciaCategoriaEnum import Categoria;

conexao = conectar()

if conexao:
    # Cria Cursor que ira popular as tabelas
    cur = conexao.cursor()
    #Populando
    # cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lunahri', 'Arcebispa')")
    # conexao.commit()

    #Populando tabela de instâncias
    instancias = [
        ("Altar do Selo",24,1,"SOLO OU GRUPO"),
        ("Infinite Space",24,0,"SOLO OU GRUPO"),
        ("Torre sem Fim",24,0,"SOLO OU GRUPO"),
        ("Ninho de Nidhogg",24,1,"SOLO OU GRUPO"),
    ]
    cur.executemany("INSERT INTO instancia (nome,recarga,moedas,categoria)VALUES(?,?,?,?)",instancias)
    cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lenahri', 'Arcebispa')")
    cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lunahri', 'Bioquimica')")
    conexao.commit()
    # data = [
    # ("Monty Python Live at the Hollywood Bowl", 1982, 7.9),
    # ("Monty Python's The Meaning of Life", 1983, 7.5),
    # ("Monty Python's Life of Brian", 1979, 8.0),
    # ]
    # cur.executemany("INSERT INTO movie VALUES(?, ?, ?)", data)
    # con.commit()  # Remember to commit the transaction after executing INSERT.

