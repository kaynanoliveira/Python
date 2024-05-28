#Implementar uma solução em Python que faça o tratamento de exceções para verificar se a entrada é, de fato, um numero.

try:
    x = int(input("Digite um número: "))
except ValueError:
    print("Entre com um numero valido.")