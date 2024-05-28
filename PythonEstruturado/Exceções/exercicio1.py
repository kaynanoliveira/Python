#Implementar uma solução em Python que faça o tratamento de exceções para verificar se a entrada é um numerica, além disso, insista que o usuário digite um numero válido.

while True:
    try:
        x = int(input("Digite um número: "))
        break
    except ValueError:
         print("Entre com um numero valido.") 