# É tudo que está em um conjunto, que não está no outro.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

# Diferença Simetrica.

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)