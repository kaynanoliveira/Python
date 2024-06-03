# Lambda, Map, Filter

lista =  [1, 5, 6, 7, 88, 90, 50]

# Elevar ao quadrado cada elemento da lista.

print(list(map(lambda x: x**2, lista)))

# Somar +5 a cada elemento da lista.

print(list(map(lambda valor: valor+5, lista)))

# Usando o Filter, filtre apenas os números pares da lista.

print(list(filter(lambda x: x % 2 == 0, lista)))

lista =  [1, -5, 6, -7, -88, 99, -50]

# Usando o método Filter, Retorne apenas os números positivos da lista.

print(list(filter(lambda valor: valor > 0, lista)))