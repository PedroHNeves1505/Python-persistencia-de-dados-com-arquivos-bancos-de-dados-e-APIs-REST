import sqlite3 as sql

conn = sql.connect('Modulo_3_Banco_de_Dados/escola.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS studants (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    idade INTEGER
)
""")

cursor.execute(
    "INSERT INTO studants (nome, idade)" \
        "VALUES (?, ?)", ('Pedro', 19))

conn.commit()

cursor.execute('SELECT * FROM studants')
print(cursor.fetchall())

conn.close()