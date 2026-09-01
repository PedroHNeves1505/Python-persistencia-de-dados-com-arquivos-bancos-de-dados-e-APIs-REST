import sqlite3 as sql

conn = sql.connect('Modulo_4_SQL_SQLite/desafio_interagindo_com_banco_de_dados/dasefio.db')
cursor = conn.cursor()

# Criar Banco de dados
cursor.execute(
    """
        CREATE TABLE IF NOT EXISTS clientes(
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT
        )
    """
)

# Adicionar clientes
cursor.execute(
    """
        INSERT INTO clientes(nome, email) VALUES(?, ?)
    """ 
)

# Listar clientes
cursor.execute(
    """
        SELECT * FROM clientes
    """
)

clientes = cursor.fetchall()

for cliente in clientes:
    print(cliente)

conn.commit()
conn.close()