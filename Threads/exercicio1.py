# Implementar uma solução em Python que faça o uso de Thread, que faça:
# A - Inicie a execução de duas Threads.
# B - Coloque a primeira e a segunda Threads para esperar, respectivamente, 3 e 2 segundos.
# C - Informe a ordem da execução das Threads.

from time import sleep
from threading import Thread

def tarefa(tempo_espera, nome_tarefa):
    print(f'\nIniciando a tarefa {nome_tarefa}')
    sleep(tempo_espera)
    print(f'Conclusão da Tarefa {nome_tarefa}')

t1 = Thread(target=tarefa, args=(3, 'A'))
t2 = Thread(target=tarefa, args=(2, 'B'))

t1.start()
t2.start()
t1.join() # esperar até completar a execução da thread 2.
t2.join() # esperar até completar a execução da thread 2.
print('A execução foi Concluida!')

