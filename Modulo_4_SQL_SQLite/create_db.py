import sqlite3 as sql

conn = sql.connect('Modulo_4_SQL_SQLite/escola.db')
cursor = conn.cursor()

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS estudantes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            idade INTEGER
        )
    """
)

cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS disciplinas(
            disciplina_id INTEGER PRIMARY KEY,
            nome TEXT,
            estudante_id INTEGER,
            FOREIGN KEY (estudante_id) \
                REFERENCES estudantes(id)
        )
    """
)

conn.commit()
conn.close()