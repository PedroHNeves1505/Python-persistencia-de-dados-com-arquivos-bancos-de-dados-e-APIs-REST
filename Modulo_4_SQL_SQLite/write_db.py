import sqlite3 as sql

conn = sql.connect('Modulo_4_SQL_SQLite/escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        INSERT INTO estudantes(nome, idade)\
        VALUES (?, ?)
    """, ('Pedro', 19)
)

conn.commit()
conn.close()