# É um conjunto onde eles não se tocam.

conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

# Conjunto A não se toca com conjunto B.
resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

# Conjunto A não se toca com conjunto C.
resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)