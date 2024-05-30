#Soma Exercício 1
a = ['10']
b = ['20']
c = ['30']
resultado = a+b+c
print(f'r = {resultado}')
#Multiplicação Exercício 2
a = ['10']
b = ['20']
c = ['30']
Resultado = a * 2 + b * 3 + c * 4 
print(f'r = {Resultado}')
#Exercício 3 
#f(x) = ax+b
#x = -b/a com a diferente de zero
a = 10
b = 5
x = -b/a
print('A raiz da equação do primeiro gráu é: x={}'. format(x))
#Formatação de dados de saida usando o metodo format()
#Exemplo de Hora
hora = 10
minutos = 26
segundos = 18
print('{} : {} : {}'.format(hora, minutos, segundos))
#Para tornar a saída formatada ainda mais intuitiva, basta utilizar a letra ‘f’ no início dos parâmetros da função print() e colocar cada variável dentro das chaves na posição em que deve ser impressa.
print(f'{hora} : {minutos} : {segundos}')