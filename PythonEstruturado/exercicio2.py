#Se a nota for maior ou igual a 7, o estudante foi aprovado.
#Se a nota for menor que 7 e maior ou igual a 5, o estudante está de Recuperação.
#Se a nota for menor que 5, o estudante está reprovado.
media = 8.5

if(media>=7.0):
    situação = "aprovado"
elif(media>=5.0):
    situação = "recuperação"
else:
    situação = "reprovado"
print(f'O estudante foi : {situação}')