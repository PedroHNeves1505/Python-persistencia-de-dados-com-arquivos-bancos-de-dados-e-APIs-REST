import sqlite3 as sql

def conectar():
    conn = sql.connect('Modulo_5_Python_e_SQL/desafio_python_e_BD/loja.db')
    cursor = conn.cursor()
    return conn, cursor

def encerrar(conn):
    conn.commit()
    conn.close()

def criar_tabela_produtos():
    conn, cursor = conectar()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS produtos(
            nome TEXT,
            preco DECIMAL
            )
        """
    )
    encerrar(conn)

def adicionar_produtos(nome, preco):
    conn, cursor = conectar()
    cursor.execute(
        """
            INSERT INTO produtos(nome, preco) VALUES(?, ?)
        """, (nome, preco)
    )
    encerrar(conn)

def listar_produtos():
    conn, cursor = conectar()
    cursor.execute(
        """
            Select * from produtos
        """
    )
    produtos = cursor.fetchall()
    for produto in produtos:
        print(f'{produto[0]:>20} -- R${produto[1]:.2f}')
    encerrar(conn)