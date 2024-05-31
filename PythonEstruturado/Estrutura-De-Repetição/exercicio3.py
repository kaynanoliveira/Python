s = 0
for i in range(5):
    s += 3*i
print(s)

#O laço for vai ser repetido cinco vezes, já que range(5) retorna a sequência (0, 1, 2, 3, 4). Vale observar que a instrução print(s) está fora do laço for, o que a levará a ser executada apenas uma vez quando o laço se encerrar. A variável s começa com valor zero e é acrescida, a cada iteração, do valor 3*i, sendo que i pertence à sequência (0, 1, 2, 3, 4). Ou seja, s recebe estes acréscimos: 0 + 3 + 6 + 9 + 12. Assim, ela termina o laço com o valor 30, que será impresso pela instrução print(s).

s = 0
a = 1
while s < 5:
      s = 3*a
      a += 1
      print(s)

#Ao ser testada pela primeira vez, a condição do while é verdadeira, já que s vale zero. Assim, a variável s recebe o valor 3 (3x1), enquanto a variável a é acrescida de uma unidade, ficando com o valor 2. Em seguida, é impresso o valor de s (3). A condição do while é então testada novamente, sendo mais uma vez verdadeira, porque s tem o valor 3 (menor que 5). Nessa iteração, a variável s recebe o valor 6 (3x2), e a variável a é acrescida de uma unidade, ficando com o valor 3. Em seguida, é impresso o valor de s (6). A condição do while é testada novamente e se revela falsa, pois s tem o valor 6 (maior que 5). Com isso, o laço while é encerrado e nada mais é impresso. Por isso, foram impressos os valores 3 e 6.