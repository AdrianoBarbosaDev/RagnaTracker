import sqlite3

conexao = sqlite3.connect('instancia.db')

cur = conexao.cursor()

# cur.execute("CREATE TABLE teste(id,nome,teste)")

cur.execute("INSERT INTO teste VALUES (1,'testenome','testeNome2')")
conexao.commit()
# cur.execute("SELECT * FROM teste")

res = cur.execute("SELECT nome FROM teste")
res.fetchall()