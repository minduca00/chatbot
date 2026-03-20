from datetime import datetime
from dados import cursor, conexao

def horarios_disponiveis(data):
    data_obj= datetime.strptime(data, '%Y-%m-%d')
    dia_semana = data_obj.weekday()  # 0: Segunda, 1: Terça, ..., 6: Domingo

    if dia_semana == 0:
        return"fechado" #segunda-feira
    elif dia_semana == 6:
        return"fechado" #domingo
    else:
        return"normal" #terça a sábado
    
def gerar_horarios_por_dia(data):
    tipo = horarios_disponiveis(data)
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

#