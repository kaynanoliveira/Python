# Construtor Set elimina os elemetos duplicados

numeros = set([1, 2, 3, 1, 3, 4, 5, 6, 5, 1])
print(numeros)  # {1, 2, 3, 4, 5, 6}

letras = set("abacaxi")
print(letras)  # {"b", "a", "c", "x", "i"}

carros = set(("palio", "gol", "celta", "palio"))
print(carros)  # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"}
print(linguagens)


# Para acessar o indice do seu Set, voce tem que transformar o seu Set em uma lista.

numeros = list(numeros)

print(numeros[0])