# Exercício Python 16: Para ter acesso a fila de prioridade, você deve ser idoso, gestante ou cadeirante. 
# Escreva um programa que pergunta a situação do usuário 
# (se é idoso, se é gestante, se é cadeirante ou nenhum destes) 
# e diga se ele pode ter acesso a fila prioridade ou não

prioridade = input("Você tem prioridade de fila? (idoso, gestante, cadeirante ou nenhum destes): ")

if prioridade.lower() == "idoso" or prioridade.lower() == "gestante" or prioridade.lower() == "cadeirante":
    print("Você tem acesso à fila de prioridade.")
else:
    print("Você não tem acesso à fila de prioridade.")
