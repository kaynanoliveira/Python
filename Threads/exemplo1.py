# Implementar uma solução em Python que faça o uso de Thread, que faça:
# A - Inicie a execução de uma Thread.
# B - Coloque a Thread para esperar 2 segundos.
# C - Informe o inicio e o final da execução Thread.

from time import sleep
from threading import Thread

def tarefa(tempo_espera, mensagem):
    print(f'\nIniciando a tarefa {mensagem}')
    sleep(tempo_espera)
    print(f'Conclusão da Tarefa {mensagem}')

thread = Thread(target=tarefa, args=(2, 'Thread em Execução'))
thread.start()

print('\nAguardando pela execução da Thread...')
thread.join()
print('Execução foi Concluida!')