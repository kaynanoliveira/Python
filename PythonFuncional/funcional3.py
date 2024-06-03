# Implementar um solução através da programação Funcional para arredondar os valores da lista de números na mesma ordem da lista de precisão.

lista_numeros = [9.56783, 7.57568, 3.00914, 6.2321]
lista_precisao = [2, 2, 3 ,3]

arredondameto = lambda x,y: round(x,y)

resultado = list(map(arredondameto, lista_numeros, lista_precisao))

print(resultado)