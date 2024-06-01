# Maiuscula, minuscula e título. 

nome = "KaYnAn"

print(nome.upper()) # Deixa tudo em maiusculo
print(nome.lower()) # Deixa tudo em minusculo
print(nome.title()) # Deixa a primeira letra em maiusculo

# Eliminando espaços em Brancos.

texto = "    Olá Mundo!     "

print(texto + ".")
print(texto.lstrip()+ ".") # Remove os espaços da esquerda
print(texto.rstrip()+ ".") # Remove os espaços da direita
print(texto.strip() + ".") # Tira os espaços da direita e da esquerda

# Junções e Centralizações.

menu = "Python"

print( "####" + menu + "####")
print(menu.center(20, "#"))
print(menu.center(14))
print(".".join(menu))