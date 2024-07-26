# Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), para escrever em um arquivo ('w'), para anexar conteúdo a um arquivo existente ("a").

# O método read retorna uma string inteira do arquivo.

# O método readline(), ler uma linha por vez, enquanto o readlines() retorna uma lista onde cada elemento é uma linha do arquivo.

arquivo = open("Manipulação De Arquivos/lorem.txt", "r")

print(arquivo.read())
print(arquivo.readlines())
print(arquivo.readline())

# Tip
# while len(linha := arquivo.readline()):
#    print(linha)



arquivo.close()