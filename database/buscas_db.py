import sqlite3
import os
from dotenv import load_dotenv
from conexao import conectar


conexao = conectar()

if conexao:
    # Cria Cursor que ira buscar as tabelas
    cur = conexao.cursor()

def buscarPersonagens():
    res = cur.execute("SELECT * FROM Personagem")
    colunas = [desc[0] for desc in res.description]
    return [dict(zip(colunas, linha)) for linha in res.fetchall()]

def buscarInstancias():
    res = cur.execute("SELECT * FROM Instancia")
    return res.fetchall()

