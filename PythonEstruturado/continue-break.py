#Essa instrução interrompe apenas a iteração corrente, fazendo com que o laço passe para a próxima iteração.
#O exemplo a seguir imprime todos os números inteiros de 1 até 10, pulando apenas o 5.
for num in range(1, 11):
    if num == 5:
        continue
    else:
        print(num)
print('Laço encerrado')

#Quando a execução do programa chega a uma instrução break, a repetição é encerrada.
#O exemplo a seguir imprime os numeros inteiros até ser igual a 5, se for igual será encerrada.
for num in range(1, 11):
    if num == 5:
        break
    else:
        print(num)
print('Laço encerrado')
