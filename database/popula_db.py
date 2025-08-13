import sqlite3
import os
from dotenv import load_dotenv
from conexao import conectar

conexao = conectar()

if conexao:
    # Cria Cursor que ira popular as tabelas
    cur = conexao.cursor()
    #Populando
    cur.execute("INSERT INTO Personagem (nome, classe) VALUES('Lunahri', 'Arcebispa')")
    conexao.commit()


