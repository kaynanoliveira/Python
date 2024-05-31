#Estratégia 1 
#Se 'a' for maior que 'b', execute: "maior = a"
#Se não, execute: "maior = b"
a = 10
b = 20
if(a>b):
    maior = a
else:
    maior = b
print(f'O maior numero é : {maior}')

#Estratégia 2 
maior = a 
if(b>maior):
    maior = b
print(f'O maior numero é : {maior}')

#Exercício 01
#Verificando se um número é impar ou par
numero = 46

if(numero%2==0):
    situação="O numero é igual a par"
else:
    situação="O numero é igual a impar"
    
print(situação)