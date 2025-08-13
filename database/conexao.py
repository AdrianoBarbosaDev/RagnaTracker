import sqlite3
import os
from pathlib import Path

# root = os.getenv("ROOT_PROJETO")

DB_PATH = Path(__file__).parent.parent / 'data' / 'RagnaTracker.db'

# PATH_DB = (f'{root}/data/RagnaTracker.db')

def conectar():
    try:
        print("Caminho para o banco:")
        print(DB_PATH)
        conn = sqlite3.connect(DB_PATH)
        return conn
    except sqlite3.Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None