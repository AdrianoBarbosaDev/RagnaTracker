import sqlite3
import os
from dotenv import load_dotenv
from conexao import conectar

conexao = conectar()

if conexao:
    # Cria Cursor que ira criar as tabelas
    cur = conexao.cursor()

    # Criacao das Tabelas
    cur.execute(
    "CREATE TABLE Instancia( " \
    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
    "nome TEXT, " \
    "recarga NUM, " \
    "moedas NUM, " \
    "categoria TEXT) "
    )

    cur.execute(
    "CREATE TABLE Personagem( " \
    "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, " \
    "nome TEXT UNIQUE, " \
    "classe TEXT) "
    )

    # cur.execute("DROP TABLE Instancia")
    # cur.execute("DROP TABLE Personagem")