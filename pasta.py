#Atribuição Multipla
a, b = 1, 2 
print("Antes da Troca")
print(f"O valor das Variaveis: a={a}, b={b}")
#Atribuição Composta
x = 10
x = x + 1
print(x)
#Primeira Troca
temp = a
a = b 
b = temp
print("Primeira Troca")
print(f"O valor das Variaveis: a={a}, b={b}")
#Segunda Troca
a, b = b, a 
print("Segunda Troca")
print(f"O valor das Variaveis: a={a}, b={b}")
#Variavel Local
def func():
    x = 1
    print(x)
#Variavel Global
x = 10
func()
print(x)    
#Função Input
nome = input('Digite seu Nome:')
print(nome)
#A função input() tanto exibe na tela a string “Digite seu Nome”, como permite que o valor informado pelo usuário seja armazenado na variável nome.

#OBS: em Python não é possível incrementar ou decrementar uma variável com um operador unário, como o ++ ou --.