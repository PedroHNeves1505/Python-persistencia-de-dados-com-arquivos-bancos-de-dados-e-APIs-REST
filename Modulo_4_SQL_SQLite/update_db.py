import sqlite3 as sql

conn = sql.connect('Modulo_4_SQL_SQLite/escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        UPDATE estudantes SET nome = ?, idade = ? WHERE id = ?
    """, ('Danielle', 20, 2)
)

conn.commit()
conn.close()