import sqlite3

def conectar():
    conexao = sqlite3.connect('dados.db')
    return conexao

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor() 

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        UNIQUE(data, horario)
    )
    ''')

    conn.commit()
    conn.close()

def inserir_agendamento(nome, data, horario):
    conn = conectar()
    cursor = conn.cursor()

    try:
        cursor.execute('''
        INSERT INTO agendamentos (nome, data, horario)
        VALUES (?, ?, ?)
        ''', (nome, data, horario))
        conn.commit()
        print("Agendamento inserido com sucesso!")
    except sqlite3.IntegrityError:
        print("Erro: Já existe um agendamento para essa data e horário.")
    finally:
        conn.close()

def horarios_ocupados(data):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('''
    SELECT horario FROM agendamentos WHERE data = ?
    ''', (data,))
    
    horarios = cursor.fetchall()
    conn.close()
    
    return [horario[0] for horario in horarios]