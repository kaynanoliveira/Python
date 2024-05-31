#Suponha que queiramos imprimir somente os números ímpares entre 1 e 10. Uma implementação possível está no emulador seguinte 

for num in range(1, 11):
    if num % 2 == 0:
        pass
    else:
        print(num)
print('Laço encerrado')

#A instrução pass atua sobre a estrutura if, permitindo que ela seja escrita sem outras instruções a serem executadas caso a condição seja verdadeira. 