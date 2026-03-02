import sqlite3

DB_NAME = "healthy_routine.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def criar_tabelas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habitos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        horas_sono REAL,
        agua_litros REAL,
        exercicio INTEGER,
        humor TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )
    """)

    conn.commit()
    conn.close()


def criar_tabela_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()


def criar_tabela_habitos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS habitos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario_id INTEGER,
        horas_sono REAL,
        agua_litros REAL,
        exercicio INTEGER,
        humor TEXT,
        FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
    )
    """)
    conn.commit()
    conn.close()


# =========================
# USUARIOS (CRUD)
# =========================

def inserir_usuarios(nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (nome) VALUES (?)", (nome,))
    conn.commit()
    conn.close()


def listar_usuarios():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM usuarios")
    usuarios = cursor.fetchall()
    conn.close()
    return usuarios


def atualizar_usuario(usuario_id, novo_nome):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE usuarios SET nome = ? WHERE id = ?",
        (novo_nome, usuario_id)
    )
    conn.commit()
    conn.close()
    print("Usuario atualizado com sucesso!")


def excluir_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()

    # exclui hábitos primeiro
    cursor.execute("DELETE FROM habitos WHERE usuario_id = ?", (usuario_id,))
    cursor.execute("DELETE FROM usuarios WHERE id = ?", (usuario_id,))

    conn.commit()
    conn.close()
    print("Usuario excluido com sucesso!")


# =========================
# HABITOS (CRUD)
# =========================

def inserir_habito(usuario_id, horas_sono, agua_litros, exercicio, humor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO habitos (usuario_id, horas_sono, agua_litros, exercicio, humor)
        VALUES (?, ?, ?, ?, ?)
    """, (usuario_id, horas_sono, agua_litros, exercicio, humor))
    conn.commit()
    conn.close()


def buscar_habitos_usuario(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT horas_sono, agua_litros, exercicio, humor
        FROM habitos
        WHERE usuario_id = ?
    """, (usuario_id,))
    habitos = cursor.fetchall()
    conn.close()
    return habitos


def listar_habitos(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT horas_sono, agua_litros, exercicio, humor
        FROM habitos
        WHERE usuario_id = ?
    """, (usuario_id,))
    dados = cursor.fetchall()
    conn.close()
    return dados


def atualizar_habito(usuario_id, horas_sono, agua_litros, exercicio, humor):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE habitos
        SET horas_sono = ?, agua_litros = ?, exercicio = ?, humor = ?
        WHERE usuario_id = ?
    """, (horas_sono, agua_litros, exercicio, humor, usuario_id))
    conn.commit()
    conn.close()
    print("Habito atualizado com sucesso!")


def excluir_habito(usuario_id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM habitos WHERE usuario_id = ?", (usuario_id,))
    conn.commit()
    conn.close()
    print("Habitos excluidos com sucesso!")
