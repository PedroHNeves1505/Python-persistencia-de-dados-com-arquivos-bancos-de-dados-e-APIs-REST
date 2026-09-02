import sqlite3 as sql

def conectar():
    conn = sql.connect('Modulo_5_Python_e_SQL/escola.db')
    return conn

def criar_tabela_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXIST estudantes(
                id INTEGER PRIMARY KEY,
                nome TEXT,
                idade INTEGER
            )
        """
    )
    conn.commit()
    conn.close()

def criar_tabela_matriculo():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS matricula(
                id INTEGER PRIMARY KEY,
                nome_matricula TEXT,
                estudante_id INTEGER,
                FOREIGN KEY (estudante_id) REFERENCES estudantes(id)
            )
        """
    )
    conn.commit()
    conn.close()

def adicionar_estudante(nome, idade):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO estudantes(nome, idade) VALUES(?, ?)
        """, (nome, idade)
    )
    conn.commit()
    conn.close()

def listar_estudantes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT * FROM estudantes
        """
    )
    estudantes = cursor.fetchall()
    for estudante in estudantes:
        print(estudante)

    conn.commit()
    conn.close()

def criar_matricula(estudante_id, nome_matricula):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            INSERT INTO matriculas(estudante_id, nome_matricula) VALUES (?, ?)
        """, (estudante_id, nome_matricula)
    )
    conn.commit()
    conn.close()

def listar_matriculas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        """
            SELECT matriculas.id, estudantes.nome, matriculas.nome_matricula FROM matriculas
            JOIN estudantes ON matriculas.estudante_id = estudante_id
        """
    )
    matriculas = cursor.fetchall()
    for matricula in matriculas:
        print(matricula)

    conn.commit()
    conn.close()