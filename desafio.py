# Crie uma Função: recomendar_plano para receber o consumo médio mensal:

    
# Crie uma Estrutura Condicional para verifica o consumo médio mensal 
# Retorne o plano de internet adequado:
    

# Solicita ao usuário que insira o consumo médio mensal de dados:
consumo = float(input("Insira seu consumo médio mensal : "))

if consumo <= 10:
    print("Plano Essencial Fibra - 50Mbps")

elif consumo <= 20:
    print("Plano Essencial Fibra - 100Mbps")
    
elif consumo <= 30:
    print("Plano Essencial Fibra - 300Mbps")
    
else:
    print("Esse plano não existe")





