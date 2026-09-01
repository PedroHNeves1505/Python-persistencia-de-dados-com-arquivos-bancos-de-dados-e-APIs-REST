import sqlite3 as sql

conn = sql.connect('Modulo_4_SQL_SQLite/escola.db')
cursor = conn.cursor()

# cursor.execute(
#     """
#         SELECT * FROM estudantes
#     """
# )

# estudantes = cursor.fetchall()

cursor.execute(
    """
        SELECT * FROM disciplinas
    """
)

disciplinas = cursor.fetchall()

conn.commit()
conn.close()

# for estudante in estudantes:
#     print(estudante)

for disciplina in disciplinas:
    print(disciplina)