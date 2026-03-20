from dados import criar_tabela, inserir_agendamento
from horarios import horarios_disponiveis
import horarios

#criar tabela
criar_tabela()

print("Bem-vindo ao sistema de agendamento barbearia Aritana!")

nome = input("Digite seu nome: ")
data = input("Digite a data desejada (YYYY-MM-DD): ")

horarios = horarios_disponiveis(data)

if isinstance(horarios, str):
    print(horarios)

else:
    print("\nhorários disponíveis:")
    for i, h in enumerate(horarios, 1):
        print(f"{i+1}. {h}")

        escolha = int(input("\nEscolha um horário pelo número: "))
        horario_escolhido = horarios[escolha - 1]

        inserir_agendamento