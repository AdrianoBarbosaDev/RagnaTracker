import sqlite3
import os
from dotenv import load_dotenv

load_dotenv() 

root = os.getenv("ROOT_PROJETO")

conexao = sqlite3.connect(f'{root}/data/RagnaTracker.db')


# Cria Cursor que ira buscar as tabelas
cur = conexao.cursor()

#Populando
res = cur.execute("SELECT * FROM Personagem")
res.fetchall()


