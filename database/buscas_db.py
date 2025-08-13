import sqlite3
import os
from dotenv import load_dotenv
from conexao import conectar

conexao = conectar()

if conexao:
    # Cria Cursor que ira buscar as tabelas
    cur = conexao.cursor()

    #Buscando
    res = cur.execute("SELECT * FROM Personagem")
    res.fetchall()


