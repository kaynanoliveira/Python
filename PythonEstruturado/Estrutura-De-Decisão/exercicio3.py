#Calcular o valor de uma compra, sendo que o preço unitario é R$10,00.

#Se for feita uma compra de até 10 unidades, não há descontos.
#Para compras entre 11 a 20 unidades é dado um desconto de 10%.
#Acima de 20 unidades, é dado um desconto de 20%.

preco_unitario = 10
DESCONTO10 = 0.1
DESCONTO20 = 0.2
quantidade = eval(input("Digite a quantidade que vai comprar: "))
if(quantidade <= 10): #menor ou igual a 10
    valor_final = preco_unitario*quantidade
elif(quantidade <= 20): #maior que 10 e menor ou igual a 20
    valor_final = preco_unitario*quantidade*(1-DESCONTO10)
else: #maior que 20
    valor_final = preco_unitario*quantidade*(1-DESCONTO20)

print(f'O valor final da compra é: {valor_final}')