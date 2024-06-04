# Implementar uma solução em Python que faça o uso de Thread, que faça:
# A - Inicie a execução de duas Threads.
# B - A primeira Thread deve calcular o cubo de um número.
# C - A primeira Thread deve calcular o quadrado de um número.
# D - Coloque a primeira e a segunda Threads para esperar, respectivamente, 3 e 2 segundos.
# E - Informe a ordem da execução das Threads.

from time import sleep
from threading import Thread

def calcular_cubo(num, tempo_espera):
    print(f'\nCubo: {num * num * num}')
    sleep(tempo_espera)
    print(f'Conclusão da função calcular_cubo')

def calcular_quadrado(num, tempo_espera):
    print(f'\nQuadrado: {num * num}')
    sleep(tempo_espera)
    print(f'Conclusão da função calcular_quadrado')

t1 = Thread(target=calcular_cubo, args=(5, 3))
t2 = Thread(target=calcular_quadrado, args=(5, 2))

t1.start()
t2.start()
t1.join() # esperar até completar a execução da thread 2.
t2.join() # esperar até completar a execução da thread 2.
print('A execução foi Concluida!')

