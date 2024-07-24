# Podemos usara write() ou writelines() para escrever em um arquivo.

arquivo = open('Manipulação De Arquivos/teste.txt', 'w')
arquivo.write("Escrevendo linha de arquivo.")
arquivo.writelines(["\n" "Escrevendo","\n" "um","\n" "novo","\n" "texto"])
arquivo.close()
