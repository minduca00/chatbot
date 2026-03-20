from datetime import datetime
from dados import horarios_ocupados
import sqlite3

conexao = sqlite3.connect('agendamentos.db')
cursor = conexao.cursor()

def tipo_dia(data):
    data_obj= datetime.strptime(data, '%Y-%m-%d')
    dia_semana = data_obj.weekday()  # 0: Segunda, 1: Terça, ..., 6: Domingo

    if dia_semana == 0:
        return"fechado" #segunda-feira
    elif dia_semana == 6:
        return"fechado" #domingo
    else:
        return"normal" #terça a sábado
    
def gerar_horarios_por_dia(data):
    tipo = tipo_dia(data)
    horarios = []

    if tipo == "fechado":
        return[]
    
    elif tipo == "domingo":
        for hora in  range(9, 12):
            horarios.append(f"{hora:02d}:00")
            horarios.append(f"{hora:02d}:30")

    else: 
        for hora in range(9, 18):
            horarios.append(f"{hora:02d}:00")
            horarios.append(f"{hora:02d}:30")
    return horarios

#horarios de almoço

def remover_horarios_almoco(horarios, data):
    if horarios_disponiveis(data) == "normal":
        bloqueados = ["12:00", "12:30", "13:00", "13:30"]
        return [h for h in horarios if h not in bloqueados]
    return horarios

#horarios disoniveis para um dia

def horarios_ocupados(data):
    cursor.execute("SELECT horario FROM agendamentos WHERE data = ?", (data,))
    resultado = cursor.fetchall()
    return [row[0] for row in resultado]

def horarios_disponiveis(data):
    tipo = tipo_dia(data)
    if tipo == "fechado":
        return "não funcionamos na segunda-feira " 
    
    horarios = gerar_horarios_por_dia(data)
    horarios = remover_horarios_almoco(horarios, data)

    ocupados = horarios_ocupados(data)

    livres = [h for h in horarios if h not in ocupados]
    return livres
        