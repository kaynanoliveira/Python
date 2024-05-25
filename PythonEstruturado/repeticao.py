#Python também permite que a repetição aconteça ao longo de uma string. Para isso, basta lembrar que a string é uma sequência de caracteres individuais.
#Suponha que você queira soletrar o nome informado pelo usuário. Uma possível implementação está demonstrada a seguir

nome = input("Entre com seu nome: \n") #Faz com que a palavra inserida pelo usuário seja armazenada na variável nome;
for letra in nome: #mostra a criação do laço, com a variável letra percorrendo a sequência de caracteres armazenada na variável nome;
    print(letra) #indica a instrução que será executada para cada repetição desse laço. O laço for executará a instrução da linha 3 tantas vezes quanto forem os elementos da sequência que está na variável nome.
