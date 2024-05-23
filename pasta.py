#Atribuição Multipla
a, b = 1, 2 
print("Antes da Troca")
print(f"O valor das Variaveis: a={a}, b={b}")
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